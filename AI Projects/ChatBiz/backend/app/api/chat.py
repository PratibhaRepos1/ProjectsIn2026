from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from ..core.database import get_db
from ..core.dependencies import get_current_user
from ..models.user import User
from ..schemas.chat import ChatMessageRequest, ChatMessageResponse, ConversationOut
from ..services.chat_service import handle_message
from ..models.conversation import Conversation

router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("/message", response_model=ChatMessageResponse)
async def chat_message(req: ChatMessageRequest, db: Session = Depends(get_db)):
    return await handle_message(db, req)


@router.get("/conversations", response_model=List[ConversationOut])
def list_conversations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return (
        db.query(Conversation)
        .options(joinedload(Conversation.messages))
        .filter(Conversation.business_id == current_user.business_id)
        .order_by(Conversation.started_at.desc())
        .limit(50)
        .all()
    )


@router.get("/history/{session_id}", response_model=ConversationOut)
def get_history(session_id: str, business_id: str, db: Session = Depends(get_db)):
    conv = db.query(Conversation).filter(
        Conversation.session_id == session_id,
        Conversation.business_id == business_id,
    ).first()
    return conv
