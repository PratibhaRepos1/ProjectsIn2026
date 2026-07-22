from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "ChatBiz API"
    debug: bool = False

    database_url: str = "postgresql://chatbiz:chatbiz@localhost:5432/chatbiz"

    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24

    upload_dir: str = "./uploads"
    max_upload_size_mb: int = 10

    default_llm_provider: str = "groq"
    groq_api_key: str = ""
    gemini_api_key: str = ""
    ollama_base_url: str = "http://localhost:11434"
    openai_api_key: str = ""
    anthropic_api_key: str = ""

    embedding_model: str = "all-MiniLM-L6-v2"
    chunk_size: int = 600
    chunk_overlap: int = 50
    retrieval_top_k: int = 4

    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
