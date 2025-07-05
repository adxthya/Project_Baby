# app/vaccine_controller.py
from app.groq_helper import ask_groq

def handle_vaccine_question(user_input):
    prompt = (
        f"[INST] You are a calm, friendly assistant specialized in Indian baby vaccination. "
        f"Answer this parent's question clearly.\n\nQuestion: {user_input} [/INST]"
    )
    return ask_groq(prompt)
