# text_bot.py
import os
from dotenv import load_dotenv
import requests

# Load GROQ API key
load_dotenv()
api_key = os.getenv("TOKEN")

def generate_reply(text):
    print("🧠 Generating reply...")

    prompt = f"[INST] You are a helpful AI assistant for baby healthcare. The user said: '{text}'. What is your response? [/INST]"

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
        return f"❌ Error: {e}"

# 🧪 Simple CLI loop
if __name__ == "__main__":
    print("🤱 Welcome to BabyCare Q&A Bot!")
    while True:
        user_input = input("👩‍🍼 Ask your question (or type 'exit'): ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Bye! Take care.")
            break

        answer = generate_reply(user_input)
        print("🤖:", answer)
