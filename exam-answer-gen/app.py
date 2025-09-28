# app.py
import streamlit as st
from summarizer import generate_answer
from utils import extract_text_from_pdf_bytes, extract_text_from_docx_bytes, word_count

st.set_page_config(page_title="MarkMate - Exam Answer Generator", layout="wide")
st.title("MarkMate — Exam Answer Generator (notes → 8/16 marks)")

st.sidebar.header("Options")
marks = st.sidebar.radio("Select marks", (8, 16))
input_type = st.sidebar.selectbox("Input type", ("Paste text", "Upload PDF", "Upload DOCX"))

notes = ""
if input_type == "Paste text":
    notes = st.text_area("Paste your class notes here", height=300)
elif input_type == "Upload PDF":
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        bytes_data = uploaded_file.read()
        notes = extract_text_from_pdf_bytes(bytes_data)
        st.text_area("Extracted text (edit if needed)", value=notes, height=300)
elif input_type == "Upload DOCX":
    uploaded_file = st.file_uploader("Upload DOCX", type=["docx"])
    if uploaded_file:
        bytes_data = uploaded_file.read()
        notes = extract_text_from_docx_bytes(bytes_data)
        st.text_area("Extracted text (edit if needed)", value=notes, height=300)

if st.button("Generate Answer"):
    if not notes.strip():
        st.error("Please provide notes (paste or upload).")
    else:
        with st.spinner("Generating answer..."):
            answer = generate_answer(notes, marks)
        st.subheader(f"Generated {marks}-marks Answer")
        st.write(answer)
        st.write("---")
        st.info(f"Word count: {word_count(answer)}")
        st.download_button("Download as TXT", answer, file_name=f"answer_{marks}marks.txt")
