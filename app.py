from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from IPython.display import display, Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Hizmet hesabı anahtar dosyasının yolunu ayarlayın
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/deniz/Desktop/chatbot/ordinal-ally-410206-88287e89ff54.json"

# API anahtarınızı alın
api_key = os.getenv("AIzaSyCyK-_djv0wHJrQV7xn0F2IVKcIGXHi-MI")

# API anahtarınızı kullanarak genai'yi yapılandırın
genai.configure(api_key=api_key)

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
