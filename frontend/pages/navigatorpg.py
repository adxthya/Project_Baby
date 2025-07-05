import streamlit as st

st.set_page_config(page_title="chAild - Select Action", layout="centered")

st.title("Choose an Option")

with open("asset/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button(" Voice Recorder", use_container_width=True):
        st.switch_page("pages/voicepg.py")

    if st.button(" Vaccine Map", use_container_width=True):
        st.switch_page("pages/vaccinepg.py")

with col2:
    if st.button(" Image Uploader", use_container_width=True):
        st.switch_page("pages/imagepg.py")

    if st.button(" Q & A", use_container_width=True):
        st.switch_page("pages/ques&ans.py")

