from pydantic import BaseModel
from datetime import datetime


class ConversationCreate(BaseModel):
    title: str = "New Chat"


class ConversationResponse(BaseModel):
    id: str
    title: str
    created_at: datetime

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    id: str
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class ConversationDetail(BaseModel):
    id: str
    title: str
    created_at: datetime
    messages: list[MessageResponse]

    class Config:
        from_attributes = True