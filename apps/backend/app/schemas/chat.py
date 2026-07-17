from typing import List

from pydantic import BaseModel

from app.schemas.message import Message


class ChatRequest(BaseModel):
    messages: List[Message]


class ChatResponse(BaseModel):
    response: str