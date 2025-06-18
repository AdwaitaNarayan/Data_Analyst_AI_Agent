import streamlit as st
import pandas as pd
import pdfplumber
import pytesseract
from PIL import Image
import docx
import matplotlib.pyplot as plt
import seaborn as sns
from together import Together
import os
import io

# API KEY
client = Together(api_key="90863deefe531b99b55eb70578c3e5bf11d9d8cec32a40f8a367075ae63dd9df")  # <-- Replace with your Together API key

# Text Extraction
def extract_text(file, file_type):
    if file_type == ".txt":
        return file.read().decode("utf-8")
    elif file_type == ".pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif file_type == ".docx":
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    elif file_type in [".png", ".jpg", ".jpeg"]:
        image = Image.open(file)
        return pytesseract.image_to_string(image)
    else:
        return "Unsupported file type for text extraction."

# Tabular Extraction
def read_tabular_data(file, file_type):
    if file_type == ".csv":
        return pd.read_csv(file)
    elif file_type == ".xlsx":
        return pd.read_excel(file)
    return None

# Ask LLM
def ask_llama(prompt):
    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[
            {"role": "system", "content": "You are a helpful data analyst."},
            {"role": "user", "content": prompt}
        ],
        stream=False
    )
    return response.choices[0].message.content

# UI
st.title("📊 Data Analyst AI Agent")

uploaded_file = st.file_uploader("Upload a document (.csv, .xlsx, .pdf, .txt, .docx, .jpg)", type=["csv", "xlsx", "pdf", "txt", "docx", "png", "jpg", "jpeg"])

if uploaded_file:
    file_type = os.path.splitext(uploaded_file.name)[1].lower()

    if file_type in [".csv", ".xlsx"]:
        df = read_tabular_data(uploaded_file, file_type)
        if df is not None:
            st.dataframe(df)

            user_question = st.text_input("Ask a question about this data")
            if user_question:
                st.info("Querying LLM...")
                prompt = f"Here's a table:\n\n{df.head(20).to_string(index=False)}\n\nQuestion: {user_question}"
                answer = ask_llama(prompt)
                st.success(answer)
    else:
        extracted_text = extract_text(uploaded_file, file_type)
        st.text_area("Extracted Text", extracted_text, height=200)

        user_question = st.text_input("Ask a question about the text above")
        if user_question:
            st.info("Querying LLM...")
            prompt = f"Here's some text:\n\n{extracted_text[:1500]}\n\nQuestion: {user_question}"
            answer = ask_llama(prompt)
            st.success(answer)
