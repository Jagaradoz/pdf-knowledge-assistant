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
    CHROMA_DB_PATH: str = "./data/chroma_db"
    COLLECTION_NAME: str = "pdf_collection"
    
    # Ingestion settings
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    
    # Embedding settings
    EMBEDDING_MODEL_NAME: str = "all-MiniLM-L6-v2"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
