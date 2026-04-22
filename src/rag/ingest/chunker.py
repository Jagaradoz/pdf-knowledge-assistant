from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.core.config import settings

def chunk_documents(documents: list[Document], chunk_size: int = None, chunk_overlap: int = None) -> list[Document]:
    """
    Splits a list of LangChain Document objects into smaller, overlapping chunks.
    """
    chunk_size = chunk_size or settings.CHUNK_SIZE
    chunk_overlap = chunk_overlap or settings.CHUNK_OVERLAP
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    
    chunks = text_splitter.split_documents(documents)
    return chunks
