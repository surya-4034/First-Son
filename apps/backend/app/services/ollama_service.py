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

    print("========== OLLAMA RESPONSE ==========")
    print(data)
    print("=====================================")

    return data["message"]["content"]


def generate_stream(messages):
    """
    Stream response from Ollama while collecting
    the complete answer.
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

    print("========== STREAM START ==========")

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        stream=True,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    full_response = ""

    for line in response.iter_lines():

        if not line:
            continue

        data = json.loads(line.decode())

        if "message" not in data:
            continue

        chunk = data["message"]["content"]

        full_response += chunk

        yield chunk

    print("========== STREAM END ==========")
    print(full_response)

def generate_conversation_title(messages) -> str:
    """
    Generate a short title based on the entire conversation.
    """

    conversation = ""

    for msg in messages:
        role = msg["role"].capitalize()
        conversation += f"{role}: {msg['content']}\n"

    prompt = f"""
You create concise chat titles.

Below is an entire conversation.

Your job:
- Summarize the overall topic.
- Use 2 to 5 words.
- Don't copy any sentence directly.
- Use nouns instead of commands.
- No quotation marks.
- No punctuation at the end.
- Return ONLY the title.

Conversation:

{conversation}
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You only generate short conversation titles.",
            },
            {
                "role": "user",
                "content": prompt,
            },
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

    title = data["message"]["content"].strip()

    title = title.split("\n")[0]
    title = title.replace('"', "").replace("'", "")
    title = title.rstrip(".!?:")

    words = title.split()

    if len(words) > 5:
        title = " ".join(words[:5])

    return title