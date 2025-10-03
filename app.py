import streamlit as st
from transformers import pipeline

# Load Hugging Face model (smaller = faster + deployable)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")  # 👈 use a smaller model

generator = load_model()

st.title("AI HTML Code Generator")
st.write("Enter a description and get HTML code!")

prompt = st.text_area("Describe the HTML you want:", "Create a simple login form.")

if st.button("Generate"):
    if prompt.strip():
        with st.spinner("Generating code..."):
            result = generator(
                prompt,
                max_length=300,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.7,
            )
        code = result[0]["generated_text"]
        st.subheader("Generated HTML Code:")
        st.code(code, language="html")

        st.subheader("Live Preview:")
        st.components.v1.html(code, height=400, scrolling=True)

        st.download_button("Download HTML", code, file_name="index.html")
    else:
        st.warning("⚠️ Please enter a description.")
