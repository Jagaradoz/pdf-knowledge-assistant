from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class QueryRequest(BaseModel):
    query: str = Field(..., example="What is the main topic of these documents?")
    llm_backend: Optional[str] = Field(default=None, example="ollama", description="LLM backend to use: 'ollama' or 'openai'.")
    model: Optional[str] = Field(default=None, example="gpt-4-turbo", description="Specific model name to use (e.g., 'gpt-4-turbo' or 'llama3').")

class SourceDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]
    score: float

class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]
