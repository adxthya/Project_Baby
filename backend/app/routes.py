# app/routes.py
from flask import Blueprint, request, jsonify
from app.qa_controller import handle_general_question
from app.vaccine_controller import handle_vaccine_question
from app.dob_handler import save_baby_profile, load_baby_profile
from app.vaccine_scheduler import generate_schedule

api = Blueprint("api", __name__)

@api.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "")
    return jsonify({"response": handle_general_question(query)})

@api.route("/vaccine", methods=["POST"])
def vaccine():
    data = request.get_json()
    query = data.get("query", "")
    return jsonify({"response": handle_vaccine_question(query)})

@api.route("/register-baby", methods=["POST"])
def register_baby():
    data = request.get_json()
    name = data.get("name")
    dob = data.get("dob")
    if not name or not dob:
        return jsonify({"error": "Name and DOB required"}), 400
    save_baby_profile(name, dob)
    return jsonify({"message": f"👶 Registered {name} born on {dob}."})

@api.route("/schedule", methods=["GET"])
def schedule():
    profile = load_baby_profile()
    if not profile:
        print("❌ No profile found in backend.")
        return jsonify({"error": "No baby registered."}), 404

    print(f"✅ Found profile: {profile}")
    schedule = generate_schedule(profile["dob"])
    return jsonify({
        "baby_name": profile["name"],
        "dob": profile["dob"],
        "schedule": schedule
    })
