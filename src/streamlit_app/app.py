import os
from pathlib import Path
import streamlit as st

# Define the folder where uploaded PDFs will be stored
PDFS_FOLDER = "/Users/justi/Downloads/DS4300/FinalProject/ds4300-final-aws/pdfs"

# Ensure the folder exists
os.makedirs(PDFS_FOLDER, exist_ok=True)

# Streamlit app
st.title("PDF Uploader")

st.write("Upload your PDF files, and they will be stored in the `pdfs` folder.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file to the pdfs folder
    file_path = Path(PDFS_FOLDER) / uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' has been uploaded successfully!")
    st.write(f"Saved to: `{file_path}`")