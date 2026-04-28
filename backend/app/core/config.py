"""Centralised settings loaded from environment variables / .env."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    log_level: str = "INFO"

    cors_origins: list[str] = [
        "http://localhost:8501",
        "http://localhost:3000",
    ]

    # LLM / RAG
    llm_provider: str = "ollama"
    llm_url: str = "http://localhost:11434"
    llm_model: str = "llama3.1"
    vector_db_url: str = ""

    # Data
    data_dir: str = "/data"


@lru_cache
def get_settings() -> Settings:
    return Settings()
