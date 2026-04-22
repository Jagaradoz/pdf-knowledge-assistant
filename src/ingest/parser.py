from langchain_community.document_loaders import PDFPlumberLoader
from langchain_core.documents import Document
import os

def extract_text_from_pdf(file_path: str) -> list[Document]:
    """
    Extracts text from a PDF file page by page using LangChain's PDFPlumberLoader.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found at: {file_path}")

    # Using lower tolerance values to prevent word concatenation in dense layouts like abstracts
    text_kwargs = {
        "x_tolerance": 1.5,
        "y_tolerance": 1.5,
    }
    loader = PDFPlumberLoader(file_path, text_kwargs=text_kwargs)
    documents = loader.load()
    
    if not documents:
        raise ValueError("No text could be extracted from the PDF. It might be a scanned image requiring OCR.")
        
    return documents
