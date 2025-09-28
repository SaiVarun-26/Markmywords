# utils.py
import pdfplumber
from docx import Document

def extract_text_from_pdf_bytes(pdf_bytes):
    text = []
    with open("temp.pdf", "wb") as f:
        f.write(pdf_bytes)
    with pdfplumber.open("temp.pdf") as pdf:
        for page in pdf.pages:
            text.append(page.extract_text() or "")
    return "\n".join(text)

def extract_text_from_docx_bytes(docx_bytes):
    with open("temp.docx", "wb") as f:
        f.write(docx_bytes)
    doc = Document("temp.docx")
    full = []
    for p in doc.paragraphs:
        full.append(p.text)
    return "\n".join(full)

def word_count(text: str):
    return len(text.split())
