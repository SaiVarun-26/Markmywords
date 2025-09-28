# summarizer.py
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import math

# Choose a CPU-friendly instruction-tuned model.
# Options: "google/flan-t5-small" (light), "google/flan-t5-base" (bigger)
MODEL_NAME = "google/flan-t5-small"

print("Loading model (this may take a moment)...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
nlp = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)  # device=-1 forces CPU

def _prompt_for_marks(notes: str, marks: int, target_words: int):
    # Clear instruction that model should use only the given notes.
    return (
        f"Using ONLY the text below, write an exam-style answer suitable for {marks} marks "
        f"(about {target_words} words). Structure it as: Introduction, Main points, Conclusion. "
        "Keep explanations clear and exam-appropriate; add one short example or application if relevant.\n\n"
        f"NOTES:\n{notes}"
    )

def generate_answer(notes: str, marks: int = 8, min_words: int = None, max_words: int = None):
    if min_words is None:
        min_words = 280 if marks == 8 else 500
    if max_words is None:
        max_words = 360 if marks == 8 else 650

    prompt = _prompt_for_marks(notes, marks, (min_words + max_words)//2)
    # Generate text. max_length refers to model tokens (rough), set generously.
    out = nlp(prompt, max_length=1024, do_sample=False)[0].get("generated_text") or nlp(prompt, max_length=1024)[0].get("generated_text")
    text = out.strip()

    words = len(text.split())
    attempts = 0
    # If too short, try to expand once with a focused expand prompt (to add examples/explanations).
    while words < int(0.9 * min_words) and attempts < 2:
        expand_prompt = (
            text + "\n\nPlease expand the answer by adding more explanation, an extra short example or an application, "
            "and a short concluding sentence. Do not add unrelated content."
        )
        out = nlp(expand_prompt, max_length=1536, do_sample=False)[0].get("generated_text")
        text = out.strip()
        words = len(text.split())
        attempts += 1

    # If too long, trim to a safe size (keeps the first part)
    if words > int(1.5 * max_words):
        tokens = text.split()
        text = " ".join(tokens[: int(1.5 * max_words)])
        # Try to finish the last sentence cleanly
        if "." in text:
            text = text.rsplit(".", 1)[0] + "."

    return text
