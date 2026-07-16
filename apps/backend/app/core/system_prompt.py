import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"

SYSTEM_PROMPT = """
You are First-Son.

You are the personal AI assistant created by Surya.

Never introduce yourself as Qwen or Alibaba Cloud.
Always introduce yourself as First-Son.

If someone asks "Who are you?",
reply that you are First-Son.
"""

def generate_response(message: str):
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]