import streamlit as st
import openai
import os
from dotenv import load_dotenv  
from pypdf import PdfReader
from io import BytesIO  

load_dotenv() # opens my .env file and reads everything inside it into memory.
openai.api_key = os.getenv("OPENAI_API_KEY") #goes into that memory, finds the variable called OPENAI_API_KEY, grabs its value which is my secret key, and hands it to the OpenAI library so it can authenticate my requests.

st.title("Serene AI: Your Personal PDF Assistant")
st.write("Upload a PDF and ask any question about its content!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")


if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    st.success("PDF uploaded successfully! Ready to answer your questions.")
    question = st.text_input("Ask a question about your PDF:")

    if question:
        with st.spinner("Serene AI is thinking..."):
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful study assistant. Answer questions based only on the provided course material."},
                    {"role": "user", "content": f"Here is the course material:\n{text}\n\nQuestion: {question}"}
                ]
            )
            answer = response.choices[0].message.content
            st.write("Serene AI:", answer)