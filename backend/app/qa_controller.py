# app/qa_controller.py
from app.groq_helper import ask_groq

def handle_general_question(user_input):
    prompt = (
        f"[INST] You are a baby healthcare assistant. "
        f"Answer the question simply.\n\nQuestion: {user_input} [/INST]"
    )
    return ask_groq(prompt)
