from abc import ABC, abstractmethod
from typing import List

_TONE_STYLES = {
    "friendly": "warm and friendly",
    "formal": "formal and professional",
    "concise": "concise and to the point",
    "playful": "playful and upbeat",
}


def tone_instruction(tone: str) -> str:
    style = _TONE_STYLES.get(tone, _TONE_STYLES["friendly"])
    return f"Respond in a {style} tone."


class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str, context: str, tone: str = "friendly") -> str:
        pass


class EmbeddingProvider(ABC):
    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        pass
