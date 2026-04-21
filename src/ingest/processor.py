import os
from ingest.parser import extract_text_from_pdf
from ingest.chunker import chunk_text
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
        1. Extract text from PDF
        2. Chunk the text
        3. Store chunks in the vector database
        
        Returns the number of chunks added.
        """
        print(f"Processing: {file_path}")
        
        # 1. Extraction
        raw_text = extract_text_from_pdf(file_path)
        
        # 2. Chunking
        chunks = chunk_text(raw_text)
        
        # 3. Storage
        # We add some basic metadata like the filename
        filename = os.path.basename(file_path)
        metadatas = [{"source": filename} for _ in chunks]
        
        self.retriever.add_chunks(chunks, metadatas=metadatas)
        
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
