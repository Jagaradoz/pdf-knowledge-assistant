import os
import sys

# Add the src directory to the python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ingest.parser import extract_text_from_pdf
from ingest.chunker import chunk_text

def main():
    pdf_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'sample.pdf')
    
    if not os.path.exists(pdf_path):
        print(f"Error: Please place a sample PDF file at {os.path.abspath(pdf_path)}")
        return

    print(f"Extracting text from: {pdf_path}...")
    try:
        raw_text = extract_text_from_pdf(pdf_path)
        print(f"Successfully extracted {len(raw_text)} characters.")
    except Exception as e:
        print(f"Extraction failed: {e}")
        return

    print("\nChunking text...")
    # Using smaller chunk size for visual verification of overlap
    chunks = chunk_text(raw_text, chunk_size=500, chunk_overlap=100)
    print(f"Created {len(chunks)} chunks.")
    
    print("\nDisplaying first 5 chunks to verify overlap:\n")
    for i, chunk in enumerate(chunks[:5]):
        print(f"--- CHUNK {i + 1} ({len(chunk)} chars) ---")
        print(chunk)
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
