import os
import sys
import glob

# Add the src directory to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ingest.processor import DocumentProcessor

def main():
    # Define paths
    raw_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    pdf_files = glob.glob(os.path.join(raw_dir, "*.pdf"))
    
    if not pdf_files:
        print(f"Error: No PDF files found in {os.path.abspath(raw_dir)}")
        return

    print(f"--- Starting Unified Ingestion Test ({len(pdf_files)} files) ---")
    
    # Initialize the processor
    # This will also initialize the VectorRetriever and local ChromaDB
    processor = DocumentProcessor()
    
    try:
        total_chunks_added = 0
        for pdf_path in pdf_files:
            # Run the full processing flow
            chunk_count = processor.process_pdf(pdf_path)
            total_chunks_added += chunk_count
            print(f"Success! Added {chunk_count} chunks from {os.path.basename(pdf_path)}.")
            
        # Verify collection count
        total_count = processor.retriever.get_collection_count()
        print(f"\nFinished! Added a total of {total_chunks_added} chunks.")
        print(f"Total items in Vector Store: {total_count}")
        
    except Exception as e:
        print(f"\nIngestion failed: {e}")

if __name__ == "__main__":
    main()
