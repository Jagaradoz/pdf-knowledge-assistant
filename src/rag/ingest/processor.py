import os
from .parser import extract_text_from_pdf
from .chunker import chunk_documents
from ..engine.retriever import VectorRetriever
from src.core.logger import logger

class DocumentProcessor:
    def __init__(self):
        """
        Initializes the DocumentProcessor with a VectorRetriever.
        """
        self.retriever = VectorRetriever()

    def process_pdf(self, file_path: str) -> int:
        """
        Orchestrates the full ingestion flow:
        1. Extract text from PDF into LangChain Documents
        2. Chunk the documents
        3. Store chunks in the vector database
        
        Returns the number of chunks added.
        """
        logger.info(f"Processing: {file_path}")
        
        # 1. Extraction
        documents = extract_text_from_pdf(file_path)
        
        # 2. Chunking
        chunks = chunk_documents(documents)
        
        # 3. Storage
        self.retriever.add_documents(chunks)
        
        return len(chunks)

def main():
    import glob
    # Simple CLI test if run directly
    processor = DocumentProcessor()
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
