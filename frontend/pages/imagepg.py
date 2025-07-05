import streamlit as st

st.set_page_config(layout="centered")

st.title(" Image Uploader")

with open("asset/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Image uploader
uploaded_file = st.file_uploader("Upload baby's Rash/Symptom image", type=["png", "jpg", "jpeg"])

# When file is uploaded
if uploaded_file is not None:
    # Preview the image
    st.image(uploaded_file, caption="Uploaded Image", width=300)

    # Show search button and wait for click
    col1, col2 = st.columns([4, 1])
    with col2:
        search_clicked = st.button(" Search", use_container_width=True)

    if search_clicked:
        with col1:
            st.success("This rash may be a mild skin irritation. Please consult a local pediatrician for confirmation.")

# 🔙 Back Button (Fixed Bottom-Left)
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
        st.switch_page("pages/navigatorpg.py")  # Make sure this is the correct filename
    container.markdown('</div>', unsafe_allow_html=True)


