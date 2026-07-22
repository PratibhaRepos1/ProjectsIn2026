from abc import ABC, abstractmethod
from typing import List


class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str, context: str) -> str:
        pass


class EmbeddingProvider(ABC):
    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        pass
