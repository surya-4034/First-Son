import json
import requests

from app.core.config import MODEL_NAME, OLLAMA_URL, TIMEOUT
from app.core.system_prompt import SYSTEM_PROMPT


def generate_response(messages):
    """
    Generate a complete response using Ollama Chat API.
    """

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            *messages,
        ],
        "stream": False,
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]


def generate_stream(messages):
    """
    Stream a response using Ollama Chat API.
    """

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            *messages,
        ],
        "stream": True,
    }
    print("Sending request to Ollama...")

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True,
        timeout=TIMEOUT,
    )

    response.raise_for_status()
    print("Connected to Ollama")

    for line in response.iter_lines():
        print(line)

        if not line:
            continue

        data = json.loads(line.decode())

        if "message" in data:
            yield data["message"]["content"]