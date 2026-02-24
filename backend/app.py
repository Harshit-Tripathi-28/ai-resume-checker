from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
import os
app = Flask(__name__)

# Proper CORS configuration
CORS(app, origins=["http://127.0.0.1:5500", "http://localhost:5500"])

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def calculate_match(resume_text, job_desc):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())
    common = resume_words.intersection(job_words)
    score = (len(common) / len(job_words)) * 100 if job_words else 0
    return round(score, 2)
@app.route("/")
def home():
    return "AI Resume Matcher Backend is Running 🚀"
@app.route("/match", methods=["POST"])
def match():
    file = request.files["resume"]
    job_desc = request.form["job_description"]

    resume_text = extract_text_from_pdf(file)
    score = calculate_match(resume_text, job_desc)

    return jsonify({"match_score": score})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)