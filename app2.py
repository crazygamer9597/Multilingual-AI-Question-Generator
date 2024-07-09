from temp import API_KEY
import streamlit as st
from langdetect import detect, LangDetectException
import google.generativeai as palm
from googletrans import Translator
import time

palm.configure(api_key=API_KEY)
translator = Translator()

def generate_questions(model_name, text):
    response = palm.generate_text(
        model=model_name,
        prompt=f"Generate questions from the following text:\n\n{text}\n\nQuestions:",
        max_output_tokens=150
    )
    questions = response.result.strip() if response.result else "No questions generated."
    return questions

def main():
    st.title("Inquisitive")

    user_text = st.text_area("Enter the text you want questions generated from:")

    detected_language = 'en' 

    try:
        if user_text.strip():
            detected_language = detect(user_text)
    except LangDetectException:
        st.warning("Language detection failed. Defaulting to English.")

    if detected_language != 'en':
        retries = 3
        for attempt in range(retries):
            try:
                translated_text = translator.translate(user_text, src=detected_language, dest='en').text
                break
            except AttributeError:
                if attempt < retries - 1:
                    time.sleep(1)
                else:
                    st.error("Translation failed after retries. Please try again later.")
                    return
        user_text = translated_text

    model_name = 'models/text-bison-001'

    if st.button("Generate Questions"):
        if user_text.strip():
            generated_questions = generate_questions(model_name, user_text)
            st.subheader("Generated Questions:")
            st.write(generated_questions)
        else:
            st.warning("Please enter some text to generate questions.")

if __name__ == "__main__":
    main()
