# ai/dob.py

import os
import json
import requests
from dotenv import load_dotenv

# Load GROQ API key
load_dotenv()
api_key = os.getenv("TOKEN")

# Directory to store baby DOBs
BABY_DATA_DIR = "ai/baby_data"
os.makedirs(BABY_DATA_DIR, exist_ok=True)

# ✅ Extract name and DOB using Groq via requests

def extract_name_and_dob(text):
    prompt = (
        f"[INST] Extract the baby's name and date of birth from this sentence: '{text}'. "
        f"Return only a valid JSON object in this exact format: {{\"name\": \"Maya\", \"dob\": \"YYYY-MM-DD\"}}. "
        f"If not found, return an empty JSON object: {{}}. [/INST]"
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

        if response.status_code != 200:
            print(f"❌ Groq API Error {response.status_code}: {response.text}")
            return {}

        content = response.json()["choices"][0]["message"]["content"].strip()
        print("🔍 Raw Groq Response:", content)

        result = json.loads(content)

        if not isinstance(result, dict) or "name" not in result or "dob" not in result:
            raise ValueError("❌ Invalid or incomplete data returned")

        return result

    except Exception as e:
        print("❌ Error parsing Groq response:", e)
        return {}




# 💾 Save DOB for a specific baby name
def save_baby_dob(name, dob):
    filename = os.path.join(BABY_DATA_DIR, f"{name.lower().strip()}.txt")
    with open(filename, "w") as f:
        f.write(dob)

# 📂 Load DOB for a specific baby name
def load_baby_dob(name):
    filename = os.path.join(BABY_DATA_DIR, f"{name.lower().strip()}.txt")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read().strip()
    return None

# 📋 List all saved babies and their DOBs
def list_all_babies():
    babies = {}
    for file in os.listdir(BABY_DATA_DIR):
        if file.endswith(".txt"):
            name = file.replace(".txt", "")
            with open(os.path.join(BABY_DATA_DIR, file), "r") as f:
                babies[name] = f.read().strip()
    return babies

