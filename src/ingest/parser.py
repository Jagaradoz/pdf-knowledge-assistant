import pdfplumber
import os

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file page by page, handling multi-column layouts 
    and preserving appropriate spacing.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found at: {file_path}")

    full_text = []
    
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            # We use a custom extraction strategy for better column handling.
            # 1. We split the page into left and right halves for 2-column papers.
            # 2. We use tolerances to ensure spaces are preserved between words.
            
            width = page.width
            height = page.height
            
            # Left column
            left_bbox = (0, 0, width / 2, height)
            left_page = page.crop(left_bbox)
            left_text = left_page.extract_text(x_tolerance=3, y_tolerance=3)
            
            # Right column
            right_bbox = (width / 2, 0, width, height)
            right_page = page.crop(right_bbox)
            right_text = right_page.extract_text(x_tolerance=3, y_tolerance=3)
            
            # Combine the columns
            page_text = ""
            if left_text:
                page_text += left_text + "\n"
            if right_text:
                page_text += right_text
                
            if page_text.strip():
                full_text.append(page_text)
            else:
                # Fallback to standard extraction if crop failed to find text 
                # (e.g. for full-width title pages)
                standard_text = page.extract_text(x_tolerance=3, y_tolerance=3)
                if standard_text:
                    full_text.append(standard_text)
                
    extracted = "\n".join(full_text)
    
    if not extracted.strip():
        raise ValueError("No text could be extracted from the PDF. It might be a scanned image requiring OCR.")
        
    return extracted
