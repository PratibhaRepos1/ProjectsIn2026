from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class LeadCreate(BaseModel):
    business_id: str
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    message: Optional[str] = None
    session_id: Optional[str] = None


class LeadUpdate(BaseModel):
    status: str


class LeadOut(BaseModel):
    id: str
    business_id: str
    name: str
    email: Optional[str]
    phone: Optional[str]
    message: Optional[str]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
