import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as palm
from langdetect import detect
from googletrans import Translator

load_dotenv()
Api_key = os.getenv("API_KEY")
palm.configure(api_key=Api_key)

translator = Translator()

def generate_questions(model_name, text):
    response = palm.generate_text(
        model=model_name,
        prompt=f"Generate questions from the following text:\n\n{text}\n\nQuestions:",
        max_output_tokens=150
    )
    questions = response.result.strip() if response.result else "No questions generated."
    return questions

i=0
model_list = palm.list_models()
for model in model_list:
    if i == 1:
        model_name = model.name
        break
    i += 1

text = input("Enter the text from which you want questions to be generated for: ")

generated_questions = generate_questions(model_name, text)
print(f"Generated Questions:\n{generated_questions}")