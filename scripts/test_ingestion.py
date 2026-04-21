import os
import sys

# Add the src directory to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ingest.processor import DocumentProcessor

def main():
    # Define paths
    pdf_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'sample.pdf')
    
    if not os.path.exists(pdf_path):
        print(f"Error: Please place a sample PDF file at {os.path.abspath(pdf_path)}")
        return

    print("--- Starting Unified Ingestion Test ---")
    
    # Initialize the processor
    # This will also initialize the VectorRetriever and local ChromaDB
    processor = DocumentProcessor()
    
    try:
        # Run the full processing flow
        chunk_count = processor.process_pdf(pdf_path)
        print(f"\nSuccess! Added {chunk_count} chunks to the vector store.")
        
        # Verify collection count
        total_count = processor.retriever.get_collection_count()
        print(f"Total items in Vector Store: {total_count}")
        
    except Exception as e:
        print(f"\nIngestion failed: {e}")

if __name__ == "__main__":
    main()
