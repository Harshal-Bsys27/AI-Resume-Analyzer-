from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PyPDF2 import PdfReader
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)
CORS(app)

# ---------------- Load Models ----------------
nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- Skill Database ----------------
SKILLS_DB = [
    "python", "java", "c++", "flask", "django", "react", "node",
    "sql", "mongodb", "machine learning", "deep learning",
    "nlp", "opencv", "data analysis", "tensorflow", "pytorch",
    "aws", "docker", "git", "linux"
]

# ---------------- Output Folder ----------------
OUTPUT_FOLDER = "../output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------- Helper Functions ----------------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "
    return text.lower()

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_skills(text):
    extracted_skills = set()
    for skill in SKILLS_DB:
        if skill in text:
            extracted_skills.add(skill)
    return list(extracted_skills)

def semantic_similarity(text1, text2):
    embeddings = model.encode([text1, text2])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 2)

# ---------------- Analysis Logic ----------------
def analyze_resume(resume_text, jd_text):
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    overall_score = semantic_similarity(resume_text, jd_text)

    # Section-wise scoring
    skills_score = ((len(matched_skills) / max(len(jd_skills), 1)) * 100)
    experience_score = semantic_similarity(resume_text[:1500], jd_text[:1500])
    education_score = 70  # baseline (can improve)

    # Strengths & Weaknesses
    strengths, weaknesses = [], []

    if skills_score >= 70:
        strengths.append("Strong technical skill match with job requirements")
    else:
        weaknesses.append("Skills mismatch with job requirements")

    if experience_score >= 65:
        strengths.append("Relevant experience aligned with job description")
    else:
        weaknesses.append("Experience section needs improvement")

    if missing_skills:
        weaknesses.append(f"Missing important skills: {', '.join(missing_skills)}")

    suggestions = [
        "Add quantified achievements in experience section",
        "Include missing skills relevant to the job role",
        "Optimize resume keywords for ATS systems"
    ]

    return {
        "overall_score": overall_score,
        "score_breakdown": {
            "skills_match": round(skills_score, 2),
            "experience_match": round(experience_score, 2),
            "education_match": education_score
        },
        "skills": {
            "resume_skills": resume_skills,
            "job_skills": jd_skills,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        },
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }

# ---------------- PDF Report ----------------
def generate_report_pdf(analysis, filename="resume_report.pdf"):
    pdf_path = os.path.join(OUTPUT_FOLDER, filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)
    y = 750
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "AI Resume Analysis Report")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Overall Match Score: {analysis['overall_score']}%")
    y -= 20

    c.drawString(50, y, f"Skills Match: {analysis['score_breakdown']['skills_match']}%")
    y -= 20
    c.drawString(50, y, f"Experience Match: {analysis['score_breakdown']['experience_match']}%")
    y -= 20
    c.drawString(50, y, f"Education Match: {analysis['score_breakdown']['education_match']}%")
    y -= 30

    c.drawString(50, y, f"Matched Skills: {', '.join(analysis['skills']['matched_skills']) if analysis['skills']['matched_skills'] else 'None'}")
    y -= 20
    c.drawString(50, y, f"Missing Skills: {', '.join(analysis['skills']['missing_skills']) if analysis['skills']['missing_skills'] else 'None'}")
    y -= 30

    c.drawString(50, y, "Strengths:")
    y -= 20
    for s in analysis['strengths']:
        c.drawString(60, y, f"- {s}")
        y -= 15

    y -= 10
    c.drawString(50, y, "Weaknesses:")
    y -= 20
    for w in analysis['weaknesses']:
        c.drawString(60, y, f"- {w}")
        y -= 15

    y -= 10
    c.drawString(50, y, "Suggestions:")
    y -= 20
    for sug in analysis['suggestions']:
        c.drawString(60, y, f"- {sug}")
        y -= 15

    c.save()
    return pdf_path

# ---------------- API Route ----------------
@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    jd = request.form.get("job_description")

    if not resume or not jd:
        return jsonify({"error": "Resume or Job Description missing"}), 400

    resume_text = extract_text_from_pdf(resume)
    analysis_result = analyze_resume(resume_text, jd)
    pdf_path = generate_report_pdf(analysis_result)

    return jsonify({
        "status": "success",
        "analysis": analysis_result,
        "pdf_report": pdf_path
    })

# ---------------- Run Server ----------------
if __name__ == "__main__":
    app.run(debug=True)
