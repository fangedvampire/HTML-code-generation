import streamlit as st
from transformers import pipeline

# Load Hugging Face model (free)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="bigcode/starcoder")

generator = load_model()

st.title("✨ AI HTML Code Generator (Free, No OpenAI API)")
st.write("Enter a description and get HTML code instantly!")

# User input
prompt = st.text_area("Describe the HTML you want:", 
                      "Create a simple responsive login form.")

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating code... please wait..."):
            result = generator(prompt, max_length=400, num_return_sequences=1, do_sample=True)
        code = result[0]["generated_text"]
        st.subheader("Generated HTML Code:")
        st.code(code, language="html")

        # Show live preview
        st.subheader("Live Preview:")
        st.components.v1.html(code, height=400, scrolling=True)

        # Download option
        st.download_button("Download HTML file", code, file_name="index.html")
    else:
        st.warning("⚠️ Please enter a description.")
