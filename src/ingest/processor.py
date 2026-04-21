import os
from ingest.parser import extract_text_from_pdf
from ingest.chunker import chunk_documents
from rag.retriever import VectorRetriever

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
        print(f"Processing: {file_path}")
        
        # 1. Extraction
        documents = extract_text_from_pdf(file_path)
        
        # 2. Chunking
        chunks = chunk_documents(documents)
        
        # 3. Storage
        self.retriever.add_documents(chunks)
        
        return len(chunks)

def main():
    # Simple CLI test if run directly
    processor = DocumentProcessor()
    sample_path = os.path.join("data", "raw", "sample.pdf")
    if os.path.exists(sample_path):
        count = processor.process_pdf(sample_path)
        print(f"Successfully processed {sample_path}: {count} chunks added.")
    else:
        print(f"Sample PDF not found at {sample_path}")

if __name__ == "__main__":
    main()
