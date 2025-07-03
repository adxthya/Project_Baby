import requests
import os
from dotenv import load_dotenv

# 🔐 Load Groq API key
load_dotenv()
api_key = os.getenv("TOKEN")

# 📅 Get vaccine schedule based on DOB and query
def get_due_vaccines(dob, query_text):
    print("📆 Fetching due vaccines using Groq...")

    prompt = (
        f"[INST] You are a helpful AI assistant that answers parent queries about baby vaccines "
        f"based on India's National Immunization Schedule. The baby was born on {dob}. "
        f"Here is the parent's query: '{query_text}'\n\n"
        f"Answer in a friendly and simple way. [/INST]"
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
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
        return f"❌ Error generating vaccine schedule: {e}"
