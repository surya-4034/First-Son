from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.conversations import router as conversation_router

from app.api.chat import router

from app.Database.database import Base, engine
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="First-Son")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(conversation_router)