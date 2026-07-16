from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ollama_service import generate_response

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):
    answer = generate_response(req.message)

    return {
        "response": answer
    }