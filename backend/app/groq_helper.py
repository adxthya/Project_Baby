# app/groq_helper.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOKEN")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def ask_groq(prompt):
    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ Groq API error: {e}"
