import requests
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Vaccine Map", layout="centered")

# Load custom CSS
with open("asset/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'> Vaccine Tracker</h1>", unsafe_allow_html=True)

# Input Form
with st.form("baby_info_form"):
    st.subheader(" Enter Baby's Details")
    baby_name = st.text_input("Baby's Name")
    dob = st.date_input("Date of Birth")
    submitted = st.form_submit_button("Submit")

# If form submitted
if submitted:
    st.success(f"Vaccine schedule for {baby_name} (DOB: {dob})")

    # 1. Register Baby
    register_url = "http://127.0.0.1:5000/register-baby"
    register_res = requests.post(register_url, json={
        "name": baby_name,
        "dob": dob.strftime("%Y-%m-%d")
    })

    if register_res.status_code == 200:
        st.success("✅ Baby profile registered successfully.")

        # 2. Get Schedule
        schedule_url = "http://127.0.0.1:5000/schedule"
        schedule_res = requests.get(schedule_url)

        if schedule_res.status_code == 200:
            schedule = schedule_res.json()["schedule"]

            # ✅ Separate completed and upcoming vaccines
            completed = [item for item in schedule if item["status"] == "✅"]
            upcoming = [item for item in schedule if item["status"] == "🕒"]

            # 💉 Vaccine Schedule Display
            st.subheader("💉 Vaccine Schedule")

            if completed:
                st.subheader("✅ Completed Vaccines")
                st.table([
                    {"Vaccine": item["vaccine"], "Date": item["due_date"], "Status": item["status"]}
                    for item in completed
                ])

            if upcoming:
                st.subheader("🕒 Upcoming Vaccines")
                st.table([
                    {"Vaccine": item["vaccine"], "Date": item["due_date"], "Status": item["status"]}
                    for item in upcoming
                ])
        else:
            st.error("❌ Could not retrieve schedule.")
    else:
        st.error("❌ Failed to register baby.")

    # Reminder toggle
    st.subheader(" Set Reminder")
    reminder = st.toggle("Enable calendar reminder notifications")
    if reminder:
        st.info(" Calendar integration will notify you before the vaccine date.")

# Fixed Back Button
st.markdown("""
    <style>
    .bottom-left {
        position: fixed;
        bottom: 20px;
        left: 20px;
        z-index: 9999;
    }
    </style>
    <div class="bottom-left">
        <form action="pages/navigatorpg.py">
            <button style="padding:10px; font-size:16px;">⬅ Back</button>
        </form>
    </div>
""", unsafe_allow_html=True)

container = st.container()
with container:
    container.markdown('<div class="bottom-left">', unsafe_allow_html=True)
    if st.button(" Back"):
        st.switch_page("pages/navigatorpg.py")  # ✅ Make sure this matches the actual filename
    container.markdown('</div>', unsafe_allow_html=True)
