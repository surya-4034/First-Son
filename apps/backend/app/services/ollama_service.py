import requests

from app.core.config import MODEL_NAME, OLLAMA_URL, TIMEOUT
from app.core.system_prompt import SYSTEM_PROMPT


def generate_response(message: str) -> str:
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