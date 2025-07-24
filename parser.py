import re
import json
import spacy
import pdfplumber
import docx
import requests

spacy_model = spacy.load("en_core_web_sm")

with open("skills.json") as f:
    SKILL_SET = json.load(f)

API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"

def query_ner(text, token):
    headers = { "Authorization": f"Bearer {token}" }
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    return response.json()

def extract_text(file):
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return "\n".join([page.extract_text() or '' for page in pdf.pages])
    elif file.name.endswith(".docx"):
        return "\n".join([p.text for p in docx.Document(file).paragraphs])
    return ""

def extract_email(text):
    match = re.findall(r"\b[\w.-]+?@\w+?\.\w+?\b", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"\+?\d[\d \-]{8,15}\d", text)
    return match[0] if match else None

def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILL_SET if skill in text_lower]

def extract_section(text, keywords):
    return [line for line in text.split('\n') if any(k in line.lower() for k in keywords)]



def parse_resume(text, hf_token):
    entities = query_ner(text, hf_token)
    return {
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
        "Education": extract_section(text, ["bachelor", "master", "phd", "degree", "university"]),
        "Experience": extract_section(text, ["2+","5+","experience", "intern", "worked", "employment"])
    }