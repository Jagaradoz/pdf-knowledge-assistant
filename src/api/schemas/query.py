from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class QueryRequest(BaseModel):
    query: str = Field(..., example="What is the main topic of these documents?")
    n_results: int = Field(default=3, ge=1, le=20)
    llm_backend: Optional[str] = Field(default=None, example="ollama", description="LLM backend to use: 'ollama' or 'openai'. Defaults to LLM_BACKEND from .env.")

class SourceDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]
    score: float

class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]
