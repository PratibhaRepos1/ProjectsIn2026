import httpx
from .base import LLMProvider
from ...core.config import settings


class OllamaProvider(LLMProvider):
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.base_url = settings.ollama_base_url

    async def generate(self, prompt: str, context: str) -> str:
        full_prompt = (
            f"You are a helpful business assistant. Use only the context below.\n\n"
            f"Context:\n{context}\n\nQuestion: {prompt}\nAnswer:"
        )
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                f"{self.base_url}/api/generate",
                json={"model": self.model, "prompt": full_prompt, "stream": False},
            )
            return response.json().get("response", "")
