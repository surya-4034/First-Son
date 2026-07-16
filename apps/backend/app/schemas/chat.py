from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import generate_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        response=generate_response(request.message)
    )