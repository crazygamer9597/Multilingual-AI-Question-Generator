from temp import API_KEY
import streamlit as st
import google.generativeai as palm
from langdetect import detect,LangDetectException
from googletrans import Translator

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

model_name = 'models/text-bison-001'
text = input("Enter the text from which you want questions to be generated for: ")

generated_questions = generate_questions(model_name, text)
print(f"Generated Questions:\n{generated_questions}")