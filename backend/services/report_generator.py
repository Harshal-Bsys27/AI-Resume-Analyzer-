from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_report_pdf(analysis_result, output_dir, filename):
    """
    Generates a PDF report from resume analysis result
    """

    pdf_path = os.path.join(output_dir, filename)

    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    y = height - 40
    line_gap = 18

    def draw_line(text):
        nonlocal y
        if y < 40:
            c.showPage()
            y = height - 40
        c.drawString(40, y, text)
        y -= line_gap

    # ---------------- Title ----------------
    draw_line("AI Resume Analysis Report")
    draw_line("=" * 50)
    y -= 10

    # ---------------- Scores ----------------
    draw_line(f"Overall Match Score: {analysis_result['overall_score']}%")
    draw_line("")

    scores = analysis_result["score_breakdown"]
    draw_line("Score Breakdown:")
    draw_line(f"- Skills Match: {scores['skills_match']}%")
    draw_line(f"- Experience Match: {scores['experience_match']}%")
    draw_line(f"- Education Match: {scores['education_match']}%")
    draw_line("")

    # ---------------- Skills ----------------
    skills = analysis_result["skills"]
    draw_line("Matched Skills:")
    draw_line(", ".join(skills["matched_skills"]) or "None")
    draw_line("")

    draw_line("Missing Skills:")
    draw_line(", ".join(skills["missing_skills"]) or "None")
    draw_line("")

    # ---------------- Strengths ----------------
    draw_line("Strengths:")
    for s in analysis_result["strengths"]:
        draw_line(f"- {s}")
    draw_line("")

    # ---------------- Weaknesses ----------------
    draw_line("Weaknesses:")
    for w in analysis_result["weaknesses"]:
        draw_line(f"- {w}")
    draw_line("")

    # ---------------- Suggestions ----------------
    draw_line("Suggestions:")
    for sug in analysis_result["suggestions"]:
        draw_line(f"- {sug}")

    c.save()
    return pdf_path
