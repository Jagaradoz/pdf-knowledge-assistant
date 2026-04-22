from fastapi import APIRouter, Depends, HTTPException
from ..schemas.query import QueryRequest, QueryResponse
from ..dependencies import get_rag_pipeline
from src.core.logger import logger

router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/", response_model=QueryResponse)
async def query_documents(
    request: QueryRequest,
    rag = Depends(get_rag_pipeline)
):
    """
    Submit a question to the RAG system and get an answer with source citations.
    """
    try:
        result = rag.answer_query(request.query, n_results=request.n_results)
        return result
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
