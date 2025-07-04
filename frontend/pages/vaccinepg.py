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

# Dummy vaccine schedule
if submitted:
    st.success(f"Vaccine schedule for {baby_name} (DOB: {dob})")

    st.subheader("💉 Vaccine Schedule")

    # Example vaccine data
    vaccine_data = [
        {"Vaccine": "BCG", "Date": "2025-07-01", "Status": "✅"},
        {"Vaccine": "Hepatitis B (1st Dose)", "Date": "2025-07-15", "Status": "🕒"},
        {"Vaccine": "OPV (Oral Polio)", "Date": "2025-08-01", "Status": "🕒"},
    ]

    # Display table
    st.table(vaccine_data)

    # Reminder toggle
    st.subheader(" Set Reminder")
    reminder = st.toggle("Enable calendar reminder notifications")

    if reminder:
        st.info(" Calendar integration will notify you before the vaccine date.")

    # Upload vaccine card
    st.subheader(" Upload Vaccine Card")
    uploaded_image = st.file_uploader("Upload vaccine card image", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Vaccine Card", use_column_width=True)

    # Export to PDF (placeholder)
    if st.button(" Export Schedule to PDF"):
        st.info("Export feature coming soon!")

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
        <form action="pages/navigator.py">
            <button style="padding:10px; font-size:16px;">⬅ Back</button>
        </form>
    </div>
""", unsafe_allow_html=True)
