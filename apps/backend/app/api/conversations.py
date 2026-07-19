from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.Database.database import get_db
from app.models.conversation import Conversation
from app.schemas.conversation import (
    ConversationCreate,
    ConversationResponse,
    ConversationDetail,
)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)


@router.post("", response_model=ConversationResponse)
def create_conversation(
    conversation: ConversationCreate,
    db: Session = Depends(get_db),
):
    new_conversation = Conversation(
        title=conversation.title,
    )

    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)

    return new_conversation


@router.get("", response_model=list[ConversationResponse])
def get_conversations(
    db: Session = Depends(get_db),
):
    return (
        db.query(Conversation)
        .order_by(Conversation.created_at.desc())
        .all()
    )


@router.get("/{conversation_id}", response_model=ConversationDetail)
def get_conversation(
    conversation_id: str,
    db: Session = Depends(get_db),
):
    conversation = (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    return conversation


@router.put(
    "/{conversation_id}",
    response_model=ConversationResponse,
)
def update_conversation(
    conversation_id: str,
    data: ConversationCreate,
    db: Session = Depends(get_db),
):
    conversation = (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found",
        )

    conversation.title = data.title

    db.commit()
    db.refresh(conversation)

    return conversation