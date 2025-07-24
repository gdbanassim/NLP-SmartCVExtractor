import streamlit as st
from parser import extract_text, parse_resume
import pandas as pd
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

st.set_page_config("Resume Parser", layout="wide")

st.title("📄 Resume Parsing Application")
st.markdown("Upload resumes and extract structured data.")

uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

if not hf_token:
    st.warning("Please set your Hugging Face token in the .env file.")
    st.stop()

if hf_token and uploaded_files:
    results = []
    for file in uploaded_files:
        with st.spinner(f"Parsing {file.name}..."):
            raw_text = extract_text(file)
            parsed = parse_resume(raw_text, hf_token)
            results.append(parsed)

    for i, res in enumerate(results):
        st.subheader(f"📌 Resume #{i+1}")
        st.json(res)

    df = pd.DataFrame(results)
    st.download_button("📥 Download JSON", json.dumps(results, indent=2), "resumes.json")
    st.download_button("📥 Download CSV", df.to_csv(index=False), "resumes.csv", "text/csv")