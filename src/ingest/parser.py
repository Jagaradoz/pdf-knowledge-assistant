import pdfplumber
import os

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file page by page.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found at: {file_path}")

    full_text = []
    
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)
                
    extracted = "\n".join(full_text)
    
    if not extracted.strip():
        raise ValueError("No text could be extracted from the PDF. It might be a scanned image requiring OCR.")
        
    return extracted
