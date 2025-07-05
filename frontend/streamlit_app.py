# Streamlit frontend app entry point.

import time
import streamlit as st

st.set_page_config(page_title="chAild AI Assistance", layout="centered")

with open("asset/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Centered, split title
st.markdown("""
    <div class="title-container">
        <div class="line1">chAild AI</div>
        <div class="line2">Assistance</div>
    </div>
""", unsafe_allow_html=True)

time.sleep(3.5)
st.switch_page("pages/navigatorpg.py")


