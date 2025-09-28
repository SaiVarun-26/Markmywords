import streamlit as st
from transformers import pipeline

# Load a text-generation model (better than summarizer for this case)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(notes, marks):
    if marks == 8:
        instruction = f"Write a detailed exam answer of about 300 words (1.5 pages) for 8 marks based on these notes:\n{notes}"
    else:
        instruction = f"Write a very detailed exam answer of about 600 words (2.5 pages) for 16 marks based on these notes:\n{notes}"

    result = generator(instruction, max_length=800, do_sample=True, temperature=0.7)
    return result[0]['generated_text']

# Streamlit UI
st.title("MarkMyWords - AI Exam Answer Generator")

notes = st.text_area("Paste your class notes here")
marks = st.radio("Select Answer Type:", ["8 Marks", "16 Marks"])

if st.button("Generate Answer"):
    with st.spinner("Generating your exam answer... ✍️"):
        answer = generate_answer(notes, 8 if marks == "8 Marks" else 16)
        st.write(answer)
