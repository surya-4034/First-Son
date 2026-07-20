from app.services.ollama_service import (
    generate_conversation_title,
)


class TitleAgent:
    """
    Generates conversation titles from the
    entire conversation history.
    """

    def generate(self, messages) -> str:

        try:
            return generate_conversation_title(
                messages
            )

        except Exception as e:

            print(f"[TitleAgent] {e}")

            return "New Chat"