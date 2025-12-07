import easyocr
from pathlib import Path

# Initialize OCR reader once
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path: str):
    """
    Returns full text + raw OCR results (bounding boxes, text, confidence)
    """
    results = reader.readtext(image_path, detail=1)
    text_lines = [r[1] for r in results]
    full_text = "\n".join(text_lines)
    return {
        "raw_results": results,
        "text": full_text,
        "lines": text_lines
    }