from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.Database.database import get_db

from app.models.message import Message
from app.models.conversation import Conversation

from app.schemas.chat import ChatRequest, ChatResponse

from app.agents.conversation_agent import ConversationAgent
from app.agents.title_agent import TitleAgent

router = APIRouter()

conversation_agent = ConversationAgent()
title_agent = TitleAgent()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    last_user = request.messages[-1]

    db.add(
        Message(
            conversation_id=request.conversation_id,
            role="user",
            content=last_user.content,
        )
    )
    db.commit()

    messages = [m.model_dump() for m in request.messages]

    answer = conversation_agent.chat(
        request.conversation_id,
        messages,
    )

    db.add(
        Message(
            conversation_id=request.conversation_id,
            role="assistant",
            content=answer,
        )
    )
    db.commit()

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.id == request.conversation_id
        )
        .first()
    )

    if conversation and conversation.title == "New Chat":
        try:
            conversation.title = title_agent.generate(
                messages
                + [
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                ]
            )

            db.commit()

        except Exception as e:
            print("Title generation failed:", e)

    return ChatResponse(response=answer)


@router.post("/chat/stream")
def stream_chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    last_user = request.messages[-1]

    db.add(
        Message(
            conversation_id=request.conversation_id,
            role="user",
            content=last_user.content,
        )
    )
    db.commit()

    messages = [m.model_dump() for m in request.messages]

    def stream_generator():
        full_response = ""

        for chunk in conversation_agent.stream(
            request.conversation_id,
            messages,
        ):
            full_response += chunk
            yield chunk

        db.add(
            Message(
                conversation_id=request.conversation_id,
                role="assistant",
                content=full_response,
            )
        )
        db.commit()

        conversation = (
            db.query(Conversation)
            .filter(
                Conversation.id == request.conversation_id
            )
            .first()
        )

        if conversation and conversation.title == "New Chat":
            try:
                conversation.title = title_agent.generate(
                    messages
                    + [
                        {
                            "role": "assistant",
                            "content": full_response,
                        }
                    ]
                )

                db.commit()

                print(
                    "Conversation renamed to:",
                    conversation.title,
                )

            except Exception as e:
                print(
                    "Title generation failed:",
                    e,
                )

    return StreamingResponse(
        stream_generator(),
        media_type="text/plain",
    )