from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import (
    generate_response,
    generate_stream,
)

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        response=generate_response(request.message)
    )


@router.post("/chat/stream")
def stream_chat(request: ChatRequest):
    return StreamingResponse(
        generate_stream(request.message),
        media_type="text/plain",
    )