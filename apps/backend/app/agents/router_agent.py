from app.services.ollama_service import (
    generate_response,
    generate_stream,
)


class RouterAgent:
    """
    Chooses which AI model/service should
    answer the request.

    For now, everything goes to Ollama.
    Later it can route to different models.
    """

    def chat(self, messages, model="default"):
        return generate_response(messages)

    def stream(self, messages, model="default"):
        return generate_stream(messages)