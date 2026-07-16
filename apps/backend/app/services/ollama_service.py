import httpx
from app.core.system_prompt import SYSTEM_PROMPT
from app.core.config import OLLAMA_HOST, OLLAMA_MODEL


class OllamaService:

    async def chat(self, message: str):

        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                f"{OLLAMA_HOST}/api/generate",
                json={
    "model": OLLAMA_MODEL,
    "system": SYSTEM_PROMPT,
    "prompt": message,
    "stream": False,
}
            )

            response.raise_for_status()

            data = response.json()

            return data["response"]


ollama_service = OllamaService()