from PIL import Image
from pytesseract import pytesseract
import os
import streamlit as st

# Set up Tesseract path (change if deployed on Linux/Mac)
TESSERACT_PATH = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = TESSERACT_PATH

# Streamlit App UI
st.title("📝 Text Extractor from Image")
st.write("Upload an image and extract text using Tesseract OCR.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Select Language
language = st.selectbox("Select OCR Language", ["eng", "rus", "ita"])

if uploaded_file:
    # Open image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text
    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image, lang=language)
        processed_text = " ".join(extracted_text.split())

    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Output", processed_text, height=200)

    # Download button
    st.download_button("Download Text", processed_text, file_name="extracted_text.txt")

st.markdown("---")
st.write("🔹 Built with [Streamlit](https://streamlit.io/) and Tesseract OCR")
