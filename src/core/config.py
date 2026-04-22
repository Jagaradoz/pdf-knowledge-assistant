import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "PDF Knowledge Assistant"
    DEBUG: bool = False
    
    # LLM Backend: "ollama" or "openai"
    LLM_BACKEND: str = "ollama"
    
    # Ollama settings
    OLLAMA_MODEL: str = "llama3"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    
    # OpenAI settings
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4-turbo"
    
    # Vector DB settings
    CHROMA_DB_PATH: str = os.path.join(os.path.dirname(__file__), "..", "..", "data", "vector_store")
    COLLECTION_NAME: str = "pdf_chunks"
    
    # Ingestion settings
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    
    # Embedding settings
    EMBEDDING_MODEL_NAME: str = "all-MiniLM-L6-v2"

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", ".env"),
        extra="ignore"
    )

settings = Settings()
