import json
import requests

from app.core.config import MODEL_NAME, OLLAMA_URL, TIMEOUT
from app.core.system_prompt import SYSTEM_PROMPT


def generate_response(message: str) -> str:
    """
    Returns the complete AI response at once.
    Used by: POST /chat
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n\nUser: {message}\nAssistant:",
        "stream": False,
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]


def generate_stream(message: str):
    """
    Streams the AI response token by token.
    Used by: POST /chat/stream
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": f"{SYSTEM_PROMPT}\n\nUser: {message}\nAssistant:",
        "stream": True,
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    for line in response.iter_lines():

        if not line:
            continue

        data = json.loads(line.decode("utf-8"))

        if "response" in data:
            yield data["response"]