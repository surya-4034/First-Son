from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.conversations import router as conversation_router
from app.api.chat import router as chat_router
from app.api.training import router as training_router
from app.core.config import CORS_ORIGIN

from app.Database.database import Base, engine
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="First-Son AI API", version="2.0")

# Support comma-separated origins from environment variables for production hosting
origins = [o.strip() for o in CORS_ORIGIN.split(",") if o.strip()]
if not origins or "*" in origins:
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/")(lambda: {"status": "online", "name": "First-Son AI API", "engine": "Google Gemini 2.0 Flash"})
app.include_router(chat_router)
app.include_router(conversation_router)
app.include_router(training_router)