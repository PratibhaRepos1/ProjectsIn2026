from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class ChatMessageRequest(BaseModel):
    business_id: str
    session_id: str
    message: str
    visitor_id: Optional[str] = None


class ChatMessageResponse(BaseModel):
    reply: str
    intent: Optional[str] = None
    confidence: Optional[float] = None
    session_id: str
    suggest_lead_capture: bool = False


class MessageOut(BaseModel):
    id: str
    sender: str
    content: str
    intent: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class ConversationOut(BaseModel):
    id: str
    session_id: str
    status: str
    started_at: datetime
    messages: List[MessageOut] = []

    class Config:
        from_attributes = True
