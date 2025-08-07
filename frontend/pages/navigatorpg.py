import streamlit as st

st.set_page_config(page_title="chAild - Select Action", layout="centered")
st.title("Choose an Option")

# Load styles
with open("asset/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Layout for vaccine and Q&A buttons
col1, col2 = st.columns(2)

with col1:
    if st.button(" Vaccine Map", use_container_width=True):
        st.switch_page("pages/vaccinepg.py")

with col2:
    if st.button(" Q & A", use_container_width=True):
        st.switch_page("pages/ques&ans.py")

# ✅ DIRECT LINK TO HTML MAP (Flask-hosted)
st.markdown("""
    <style>
    .icon-button {
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }
    </style>

    <div class="icon-button">
        <a href="http://localhost:8080/static/vaccine_map.html" target="_blank">
            <img src="https://cdn3.iconfinder.com/data/icons/glypho-free/64/map-pin-marker-circle-128.png" width="100" />
        </a>
    </div>
""", unsafe_allow_html=True)
