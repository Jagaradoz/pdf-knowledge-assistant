import os
import glob
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.rag.retriever import VectorRetriever
from src.core.config import settings
from src.core.logger import logger

def extract_text_from_pdf(file_path: str) -> list[Document]:
    """Extracts text from a PDF file page by page."""
    if not os.path.exists(file_path):
        logger.error(f"PDF file not found at: {file_path}")
        raise FileNotFoundError(f"PDF file not found at: {file_path}")

    text_kwargs = {"x_tolerance": 1.5, "y_tolerance": 1.5}
    loader = PDFPlumberLoader(file_path, text_kwargs=text_kwargs)
    documents = loader.load()
    
    if not documents:
        raise ValueError("No text could be extracted from the PDF.")

    for doc in documents:
        doc.metadata['source'] = os.path.basename(file_path)
        
    return documents

def chunk_documents(documents: list[Document]) -> list[Document]:
    """Splits Documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

class DocumentProcessor:
    def __init__(self):
        self.retriever = VectorRetriever()

    def process_pdf(self, file_path: str) -> int:
        logger.info(f"Processing: {file_path}")
        documents = extract_text_from_pdf(file_path)
        chunks = chunk_documents(documents)
        self.retriever.add_documents(chunks)
        return len(chunks)

def main():
    processor = DocumentProcessor()
    # Path relative to the project root
    raw_dir = os.path.join("data", "raw")
    pdf_files = glob.glob(os.path.join(raw_dir, "*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {raw_dir}")
        return

    total_chunks = 0
    print(f"Found {len(pdf_files)} PDF(s) to process.")
    for pdf_path in pdf_files:
        try:
            count = processor.process_pdf(pdf_path)
            total_chunks += count
            print(f"Successfully processed {os.path.basename(pdf_path)}: {count} chunks added.")
        except Exception as e:
            print(f"Failed to process {os.path.basename(pdf_path)}: {e}")
            
    print(f"\nProcessing complete! Added a total of {total_chunks} chunks to the database.")

if __name__ == "__main__":
    main()
