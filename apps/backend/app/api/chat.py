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
        response=generate_response(
            [m.model_dump() for m in request.messages]
        )
    )


@router.post("/chat/stream")
def stream_chat(request: ChatRequest):

    return StreamingResponse(
        generate_stream(
            [m.model_dump() for m in request.messages]
        ),
        media_type="text/plain",
    )