"""
Configurations for the application
Uses pydantic settings for validated environment variables and default values
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    # Openai API key for prod but using ollama for local dev
    primary_model: str = "llama3.1:8b"
    fallback_model: str = "llama3.2:3b"
    embedding_model: str = "nomic-embed-text"

    # langsmith 
    langchain_tracing_v2 :bool = True
    langchain_api_key: str = ""
    langchain_project: str = "production-api"

    #application
    app_env: str = "production"
    log_level: str = "INFO"
    ratelimit: str = "20/minute"
    cache_ttl_seconds: int = 300
    max_retries: int = 3

    model_config= {"env_file": ".env","extra": "ignore"}

    @property
    def is_production(self) -> bool:
        """Check if the application is running in production environment"""
        return self.app_env == "production"


@lru_cache()
def get_settings() -> Settings:
    """Get the application settings with caching to avoid reloading"""
    return Settings()
