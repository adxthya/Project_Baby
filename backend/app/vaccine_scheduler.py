# app/vaccine_scheduler.py
from datetime import datetime, timedelta

VACCINES = [
    {"name": "BCG", "weeks": 0},
    {"name": "Hepatitis B", "weeks": 0},
    {"name": "DPT-1", "weeks": 6},
    {"name": "DPT-2", "weeks": 10},
    {"name": "MMR", "weeks": 36}
]

def generate_schedule(dob_str):
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    schedule = []
    for vac in VACCINES:
        due = dob + timedelta(weeks=vac["weeks"])
        schedule.append({
            "vaccine": vac["name"],
            "due_date": due.strftime("%Y-%m-%d")
        })
    return schedule
