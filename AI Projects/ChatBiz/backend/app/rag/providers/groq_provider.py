from .base import LLMProvider
from ...core.config import settings


class GroqProvider(LLMProvider):
    def __init__(self, model: str = "llama-3.1-8b-instant"):
        self.model = model
        self._client = None

    def _get_client(self):
        if not self._client:
            from groq import AsyncGroq
            self._client = AsyncGroq(api_key=settings.groq_api_key)
        return self._client

    async def generate(self, prompt: str, context: str) -> str:
        client = self._get_client()
        system = (
            "You are a helpful business assistant. Answer questions using only the provided context. "
            "If the context doesn't contain enough information, say so politely and offer to connect the user with the team."
        )
        user_message = f"Context:\n{context}\n\nQuestion: {prompt}"
        response = await client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_message},
            ],
            max_tokens=512,
        )
        return response.choices[0].message.content
