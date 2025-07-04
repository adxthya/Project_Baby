import streamlit as st

st.set_page_config(layout="centered")

st.title(" Voice Recorder")

with open("asset/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.write("This page will contain the voice recording feature.")

# 🔵 Voice note image (centered with white circular border)
st.markdown("""
    <style>
    .voice-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        margin-bottom: 80px;
    }
    .voice-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 5px solid white;
        object-fit: cover;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    }
    </style>
    <div class="voice-image-container">
        <img src="https://cdn4.iconfinder.com/data/icons/basic-ui-2-line/32/microphone-mic-speak-voice-recorder-128.png" class="voice-image" />
    </div>
""", unsafe_allow_html=True)

# ⬅️ Fixed bottom-left Back button
st.markdown("""
    <style>
    .bottom-left {
        position: fixed;
        bottom: 20px;
        left: 20px;
        z-index: 9999;
    }
    </style>
""", unsafe_allow_html=True)

container = st.container()
with container:
    container.markdown('<div class="bottom-left">', unsafe_allow_html=True)
    if st.button(" Back"):
        st.switch_page("pages/navigator.py")  # ✅ Make sure this matches the actual filename
    container.markdown('</div>', unsafe_allow_html=True)

