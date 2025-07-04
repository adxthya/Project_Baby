import streamlit as st

st.title(" Q & A Section")

with open("asset/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.write("Ask questions related to baby care.")
user_input = st.text_input("Ask a question:")
if user_input:
    st.write("Answer will appear here...")

# At the end of 2_voice.py or other pages
# ... your content ...

# Add back button


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
        st.switch_page("pages/navigator.py")
    container.markdown('</div>', unsafe_allow_html=True)
