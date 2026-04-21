from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_documents(documents: list[Document], chunk_size: int = 1000, chunk_overlap: int = 100) -> list[Document]:
    """
    Splits a list of LangChain Document objects into smaller, overlapping chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    
    chunks = text_splitter.split_documents(documents)
    return chunks
