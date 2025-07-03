import os
import re
from dotenv import load_dotenv
from dob import extract_name_and_dob, save_baby_dob, load_baby_dob
from vaccine_bot import answer_vaccine_question
from vaccine_scheduler import get_due_vaccines

# Load environment variables
load_dotenv()

# 🧠 Classify user input
def classify_intent(text):
    text = text.lower()
    if "born" in text or "birthday" in text or "date" in text:
        return "dob"
    elif "due" in text or "next" in text or "when" in text:
        return "schedule"
    else:
        return "faq"

# 💬 Main Loop
if __name__ == "__main__":
    print("👶 Welcome to Baby Vaccine Assistant!")
    
    while True:
        user_input = input("\n🧑‍🍼 Ask your question (or type 'exit' to quit): ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        intent = classify_intent(user_input)

        if intent == "dob":
            info = extract_name_and_dob(user_input)
            print("🧾 Parsed:", info)

            if isinstance(info, dict) and "name" in info and "dob" in info:
                name, dob = info["name"], info["dob"]
                save_baby_dob(name, dob)
                print(f"✅ Saved! Baby {name}'s date of birth is {dob}.")
            else:
                print("❌ Could not extract name and DOB properly. Please try again.")

        elif intent == "schedule":
            name_match = re.search(r"\b(for|of)\s+(\w+)", user_input)
            if name_match:
                name = name_match.group(2)
                dob = load_baby_dob(name)
                if dob:
                    response = get_due_vaccines(dob, user_input)
                else:
                    response = f"I don't have the birth date for {name}. Please tell me first."
            else:
                response = "Please mention your baby's name in the question to check the schedule."
            print("📅", response)

        else:
            reply = answer_vaccine_question(user_input)
            print("💡", reply)
