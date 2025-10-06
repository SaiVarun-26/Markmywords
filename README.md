# MarkMyWords

**MarkMyWords** is an AI-powered exam answer generator designed to help students create well-structured answers from their class notes. You can upload your notes, choose the marks (8 or 16), and receive a detailed answer instantly.

This project uses **Streamlit** for the web interface and **Hugging Face Transformers** for AI-generated text.

---

# Features

- **Paste Notes:** Enter your class notes in plain text.  
- **Customizable Answer Length:** Select either **8 marks** (about 300 words) or **16 marks** (about 600 words) answers.  
- **AI-Generated Answers:** Generates detailed, structured, and easy-to-read answers appropriate for exams.  
- **Fast and Interactive:** User-friendly web interface using Streamlit.  

---

# How It Works

1. **Paste Notes:** Copy your class notes into the text area.  
2. **Select Marks:** Choose either **8 Marks** or **16 Marks** answer type.  
3. **Generate Answer:** Click the **Generate Answer** button to get a detailed AI-generated answer.  

---

# Technologies Used

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) for the web interface  
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) using the `google/flan-t5-base` model for text generation  

---

# Installation

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/MarkMyWords.git
cd MarkMyWords
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
