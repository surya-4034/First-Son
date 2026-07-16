from fastapi import FastAPI
from pydantic import BaseModel

from app.services.ollama_service import ollama_service

app = FastAPI(
    title="First-Son API",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "project": "First-Son",
        "status": "Running",
    }


@app.post("/chat")
async def chat(request: ChatRequest):

    answer = await ollama_service.chat(request.message)

    return {
        "response": answer
    }