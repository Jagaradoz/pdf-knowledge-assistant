import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str
    DEBUG: bool = False
    
    # LLM Backend: "ollama" or "openai"
    LLM_BACKEND: str
    
    # Ollama settings
    OLLAMA_MODEL: str
    OLLAMA_BASE_URL: str
    
    # OpenAI settings
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str
    
    # Vector DB settings
    CHROMA_DB_PATH: str = os.path.join(os.path.dirname(__file__), "..", "..", "data", "vector_store")
    COLLECTION_NAME: str
    
    # Ingestion settings
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int
    
    # Embedding settings
    EMBEDDING_MODEL_NAME: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", ".env"),
        extra="ignore"
    )

settings = Settings()
