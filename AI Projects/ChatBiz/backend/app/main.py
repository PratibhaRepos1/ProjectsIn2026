from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from .core.config import settings
from .core.database import Base, engine
from .api import auth, businesses, faqs, documents, products, chat, leads, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(businesses.router)
app.include_router(faqs.router)
app.include_router(documents.router)
app.include_router(products.router)
app.include_router(chat.router)
app.include_router(leads.router)
app.include_router(analytics.router)

os.makedirs(settings.upload_dir, exist_ok=True)


@app.get("/health")
def health():
    return {"status": "ok"}
