import os
import sys

# Add the src directory to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ingest.parser import extract_text_from_pdf
from ingest.chunker import chunk_text
from rag.retriever import VectorRetriever

def main():
    pdf_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'sample.pdf')
    
    if not os.path.exists(pdf_path):
        print(f"Error: Please place a sample PDF file at {os.path.abspath(pdf_path)}")
        return

    print("Phase 1: Extracting and chunking...")
    raw_text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(raw_text, chunk_size=500, chunk_overlap=100)
    print(f"Created {len(chunks)} chunks from {pdf_path}.")

    print("\nPhase 2: Generating embeddings and storing in ChromaDB...")
    
    # Initialize retriever
    retriever = VectorRetriever()
    
    # Add chunks to vector store
    # We can add some basic metadata like source file
    metadatas = [{"source": "sample.pdf"} for _ in chunks]
    
    print("Embedding chunks and inserting into database (this might take a moment the first time as it downloads the model)...")
    retriever.add_chunks(chunks, metadatas=metadatas)
    
    # Verify count
    count = retriever.get_collection_count()
    print(f"\nSuccess! The vector store collection now contains {count} items.")
    print(f"Check the 'data/vector_store/' directory to see the generated database files.")

if __name__ == "__main__":
    main()
