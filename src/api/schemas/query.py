from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class QueryRequest(BaseModel):
    query: str = Field(..., example="What is the main topic of these documents?")
    n_results: int = Field(default=5, ge=1, le=20)

class SourceDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]
    score: float

class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]
