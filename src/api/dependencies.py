from ..rag.engine.pipeline import rag_pipeline

def get_rag_pipeline():
    """
    Dependency to provide the RAG pipeline instance.
    """
    return rag_pipeline
