from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question) -> any:
    response = model.generate_content(question)
    return response.text

## Intialize our Streamlit app
st.set_page_config(page_title = "Smart Bot")
st.header("My Virtual Friend")

input = st.text_input("Input :", key = "input")
submit = st.button("Ask your question")

if submit :
    response = get_gemini_response(input)
    st.subheader(" The response is :")
    st.write(response)

