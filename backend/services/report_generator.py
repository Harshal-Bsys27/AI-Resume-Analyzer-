import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_report_pdf(analysis, output_dir, filename="resume_report.pdf"):
    pdf_path = os.path.join(output_dir, filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

    y = 750
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "AI Resume Analysis Report")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Overall Match Score: {analysis['overall_score']}%")
    y -= 20

    scores = analysis["score_breakdown"]
    c.drawString(50, y, f"Skills Match: {scores['skills_match']}%")
    y -= 20
    c.drawString(50, y, f"Experience Match: {scores['experience_match']}%")
    y -= 20
    c.drawString(50, y, f"Education Match: {scores['education_match']}%")
    y -= 30

    skills = analysis["skills"]
    c.drawString(
        50, y,
        f"Matched Skills: {', '.join(skills['matched_skills']) or 'None'}"
    )
    y -= 20
    c.drawString(
        50, y,
        f"Missing Skills: {', '.join(skills['missing_skills']) or 'None'}"
    )
    y -= 30

    c.drawString(50, y, "Strengths:")
    y -= 20
    for s in analysis["strengths"]:
        c.drawString(60, y, f"- {s}")
        y -= 15

    y -= 10
    c.drawString(50, y, "Weaknesses:")
    y -= 20
    for w in analysis["weaknesses"]:
        c.drawString(60, y, f"- {w}")
        y -= 15

    y -= 10
    c.drawString(50, y, "Suggestions:")
    y -= 20
    for sug in analysis["suggestions"]:
        c.drawString(60, y, f"- {sug}")
        y -= 15

    c.save()
    return pdf_path
