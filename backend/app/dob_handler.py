# app/dob_handler.py
import json
import os

PROFILE_FILE = "baby_profile.json"

def save_baby_profile(name, dob):
    with open(PROFILE_FILE, "w") as f:
        json.dump({"name": name, "dob": dob}, f)

def load_baby_profile():
    if not os.path.exists(PROFILE_FILE):
        return None
    with open(PROFILE_FILE, "r") as f:
        return json.load(f)
