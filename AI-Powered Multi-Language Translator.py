import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "your-openai-api-key"

st.set_page_config(page_title="Generative AI-powered Translator")

# Title
st.title("Generative AI-powered Translator")

# Input text
input_text = st.text_area("Enter text to translate:", height=150)

# Language options
languages = ["English", "French", "Spanish", "German", "Hindi"]
source_lang = st.selectbox("From", languages, index=0)
target_lang = st.selectbox("To", languages, index=1)

# Translate button
if st.button("Translate") and input_text.strip() != "":
    with st.spinner("Translating..."):
        prompt = (
            f"Translate the following text from {source_lang} to {target_lang}. "
            f"Preserve the context and tone:\n\n{input_text}"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            translation = response['choices'][0]['message']['content']
            st.text_area("Translated Text:", translation, height=150)
        except Exception as e:
            st.error(f"Error: {str(e)}")
