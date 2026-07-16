import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "first-son:latest"


def generate_response(message: str):
    payload = {
        "model": MODEL,
        "prompt": message,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()

    return data["response"]