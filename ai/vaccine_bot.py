import requests
import os
from dotenv import load_dotenv

# 🔐 Load API key from .env
load_dotenv()
api_key = os.getenv("TOKEN")

def answer_vaccine_question(question):
    print("💬 Answering vaccine-related question using Groq...")

    prompt = (
        f"[INST] You are a calm, friendly assistant specialized in Indian baby vaccination. "
        f"Please answer this parent's question in a simple, understandable tone.\n\n"
        f"Question: {question}\n\nAnswer: [/INST]"
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",  # ✅ Or your preferred model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        reply = response.json()["choices"][0]["message"]["content"]
        return reply.strip()

    except Exception as e:
        return f"❌ Error generating reply: {e}"