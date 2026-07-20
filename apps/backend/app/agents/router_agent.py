from app.services.ollama_service import (
    generate_response,
    generate_stream,
)


class RouterAgent:
    """
    Routes requests to the appropriate AI model.

    Currently:
        • Ollama

    Future:
        • Qwen
        • DeepSeek
        • Llama
        • Gemma
        • Phi
        • Mistral
        • OpenAI
        • Claude
        • Google Gemini
    """

    def chat(
        self,
        messages: list,
        model: str = "default",
    ):

        if model == "default":
            return generate_response(messages)

        elif model == "reasoning":
            return generate_response(messages)

        elif model == "vision":
            return generate_response(messages)

        elif model == "coding":
            return generate_response(messages)

        else:
            return generate_response(messages)

    def stream(
        self,
        messages: list,
        model: str = "default",
    ):

        if model == "default":
            return generate_stream(messages)

        elif model == "reasoning":
            return generate_stream(messages)

        elif model == "vision":
            return generate_stream(messages)

        elif model == "coding":
            return generate_stream(messages)

        else:
            return generate_stream(messages)