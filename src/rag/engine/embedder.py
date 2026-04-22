from langchain_huggingface import HuggingFaceEmbeddings
from src.core.config import settings

def get_embeddings_model() -> HuggingFaceEmbeddings:
    """
    Returns a configured LangChain HuggingFaceEmbeddings instance.
    """
    return HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL_NAME)
