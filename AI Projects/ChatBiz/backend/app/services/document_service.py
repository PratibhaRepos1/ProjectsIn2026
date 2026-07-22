import os
import json
import uuid
from typing import List
from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException
from ..models.document import Document, DocumentChunk
from ..core.config import settings
from ..rag.embeddings import embed_texts


ALLOWED_TYPES = {"pdf", "docx", "txt", "csv"}


def _extract_text(path: str, file_type: str) -> str:
    if file_type == "txt" or file_type == "csv":
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    if file_type == "pdf":
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(path)
            return "\n".join(p.extract_text() or "" for p in reader.pages)
        except Exception:
            return ""
    if file_type == "docx":
        try:
            import docx
            doc = docx.Document(path)
            return "\n".join(p.text for p in doc.paragraphs)
        except Exception:
            return ""
    return ""


def _chunk_text(text: str, size: int, overlap: int) -> List[str]:
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunk = " ".join(words[i : i + size])
        chunks.append(chunk)
        i += size - overlap
    return chunks


async def ingest_document(
    db: Session, business_id: str, user_id: str, file: UploadFile
) -> Document:
    ext = (file.filename or "").rsplit(".", 1)[-1].lower()
    if ext not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail=f"File type .{ext} not supported")

    content = await file.read()
    if len(content) > settings.max_upload_size_mb * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    os.makedirs(settings.upload_dir, exist_ok=True)
    saved_name = f"{uuid.uuid4()}.{ext}"
    saved_path = os.path.join(settings.upload_dir, saved_name)
    with open(saved_path, "wb") as f:
        f.write(content)

    doc = Document(
        business_id=business_id,
        filename=file.filename,
        file_url=saved_path,
        file_type=ext,
        status="processing",
        uploaded_by=user_id,
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    _process_document(db, doc, saved_path, ext)
    return doc


def _process_document(db: Session, doc: Document, path: str, ext: str):
    try:
        text = _extract_text(path, ext)
        chunks = _chunk_text(text, settings.chunk_size, settings.chunk_overlap)
        embeddings = embed_texts(chunks)

        for idx, (chunk_text, emb) in enumerate(zip(chunks, embeddings)):
            chunk = DocumentChunk(
                business_id=doc.business_id,
                document_id=doc.id,
                chunk_index=idx,
                content=chunk_text,
                embedding_json=json.dumps(emb),
            )
            db.add(chunk)

        doc.status = "embedded"
    except Exception:
        doc.status = "failed"
    finally:
        db.commit()
