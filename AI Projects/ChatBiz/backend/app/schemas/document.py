from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class DocumentOut(BaseModel):
    id: str
    business_id: str
    filename: str
    file_url: str
    file_type: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
