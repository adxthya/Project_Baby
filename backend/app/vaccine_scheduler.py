from datetime import datetime, timedelta  # ✅ Include timedelta

def generate_schedule(dob):
    dob = datetime.strptime(dob, "%Y-%m-%d")
    schedule = [
        ("BCG", 0),
        ("Hepatitis B", 0),
        ("DPT-1", 42),
        ("DPT-2", 70),
        ("MMR", 252)
    ]

    result = []
    today = datetime.today()
    for vaccine, days_after in schedule:
        due_date = dob + timedelta(days=days_after)  # ✅ Requires timedelta
        status = "✅" if due_date < today else "🕒"
        result.append({
            "vaccine": vaccine,
            "due_date": due_date.strftime("%Y-%m-%d"),
            "status": status
        })
    return result
