import fitz
# pdf_processor/utils.py
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    # Your extraction logic here
    pass

def process_pdf(pdf_path):
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text += page.get_text()

        return text
    except Exception as e:
        return f"Error processing PDF: {e}"
    finally:
        pdf_document.close()
