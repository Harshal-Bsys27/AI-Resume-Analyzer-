from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import simpleSplit
import os

def draw_logo(c, width, y):
    # Large logo initials
    c.setFont("Helvetica-Bold", 44)
    c.setFillColorRGB(1, 0.6, 0.1)
    c.drawCentredString(width / 2, y, "HireLens")
    # Subtitle
    c.setFont("Helvetica-Bold", 18)
    c.setFillColorRGB(0.2, 0.2, 0.2)
    c.drawCentredString(width / 2, y - 32, "ATS Resume Analyzer Report")
    # Divider
    c.setStrokeColorRGB(1, 0.6, 0.1)
    c.setLineWidth(3)
    c.line(width * 0.25, y - 45, width * 0.75, y - 45)
    c.setFillColorRGB(0, 0, 0)

def draw_wrapped_text(c, text, x, y, max_width, font="Helvetica", font_size=12, color=colors.black, line_height=15):
    c.setFont(font, font_size)
    c.setFillColor(color)
    lines = simpleSplit(text, font, font_size, max_width)
    for line in lines:
        if y < 60:
            c.showPage()
            y = letter[1] - 40
        c.drawString(x, y, line)
        y -= line_height
    return y

def draw_tag_list(c, label, items, x, y, color, width):
    if not items:
        return y
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(color)
    y = draw_wrapped_text(c, label, x, y, width - x - 20)
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    tag_line = ", ".join(items)
    y = draw_wrapped_text(c, tag_line, x + 20, y, width - x - 40)
    y -= 5
    return y

def generate_report_pdf(analysis_result, output_dir, filename):
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Branding & Logo
    y = height - 60
    draw_logo(c, width, y)
    y -= 80

    # Summary Section
    c.setFont("Helvetica-Bold", 15)
    c.setFillColorRGB(1, 0.6, 0.1)
    c.drawString(40, y, "Summary & Key Insights:")
    y -= 22
    summary = analysis_result.get("summary", "No summary available.")
    y = draw_wrapped_text(c, summary, 60, y, width - 100)
    y -= 10

    # Resume & Role Details
    selected_role = analysis_result.get("selected_role") or analysis_result.get("role_detected") or "Not Provided"
    role_detected = analysis_result.get("role_detected") or analysis_result.get("selected_role") or "Not Detected"
    profile_type = analysis_result.get("profile_type", "General")
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(colors.orange)
    c.drawString(40, y, "Resume & Role Details:")
    y -= 18
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    y = draw_wrapped_text(c, f"Role Selected: {selected_role}", 60, y, width - 80)
    y = draw_wrapped_text(c, f"Role Detected: {role_detected}", 60, y, width - 80)
    y = draw_wrapped_text(c, f"Profile Type: {profile_type}", 60, y, width - 80)
    y = draw_wrapped_text(c, f"Overall ATS Score: {analysis_result.get('overall_score', 0)}%", 60, y, width - 80)
    y = draw_wrapped_text(c, f"Tech Stack Coverage: {analysis_result.get('techstack_coverage', 0)}%", 60, y, width - 80)
    breakdown = analysis_result.get("score_breakdown", {})
    y = draw_wrapped_text(c, f"Skills Match: {breakdown.get('skills_match', 0)}%", 60, y, width - 80)
    y = draw_wrapped_text(c, f"Experience Match: {breakdown.get('experience_match', 0)}%", 60, y, width - 80)
    y = draw_wrapped_text(c, f"Education Match: {breakdown.get('education_match', 0)}%", 60, y, width - 80)
    y -= 10

    # Show what resume actually has (detected skills, soft skills, certifications)
    skills = analysis_result.get("skills", {})
    y = draw_tag_list(
        c, "Detected Technical Skills:", [s for s in skills.get("matched_skills", []) if "No " not in s], 60, y, colors.green, width
    )
    y = draw_tag_list(
        c, "Detected Soft Skills:", [s for s in skills.get("matched_soft_skills", []) if "No " not in s], 60, y, colors.blue, width
    )
    y = draw_tag_list(
        c, "Detected Certifications:", [s for s in skills.get("matched_certifications", []) if "No " not in s], 60, y, colors.purple, width
    )
    y -= 10

    # Strengths, Weaknesses, Suggestions, Feedback, Flaws
    def draw_list_section(title, items):
        nonlocal y
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(colors.orange)
        y = draw_wrapped_text(c, f"{title}:", 40, y, width - 80)
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        for item in items:
            if item:
                y = draw_wrapped_text(c, f"- {item}", 60, y, width - 100)
        y -= 10

    draw_list_section("Strengths", analysis_result.get("strengths", []))
    draw_list_section("Weaknesses", analysis_result.get("weaknesses", []))
    draw_list_section("Suggestions & Action Steps", analysis_result.get("suggestions", []))
    draw_list_section("Feedback", analysis_result.get("feedback", []))
    draw_list_section("Detected Flaws", analysis_result.get("flaws", []))

    # Key Responsibilities for this Role
    key_resp = analysis_result.get("key_responsibilities", [])
    if key_resp:
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(colors.orange)
        y = draw_wrapped_text(c, "Key Responsibilities for this Role:", 40, y, width - 80)
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        for item in key_resp:
            y = draw_wrapped_text(c, f"- {item}", 60, y, width - 100)
        y -= 10

    # Recommended Keywords for this Role
    keywords = analysis_result.get("recommended_keywords", [])
    if keywords:
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(colors.orange)
        y = draw_wrapped_text(c, "Keywords for this Role:", 40, y, width - 80)
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        y = draw_wrapped_text(c, ", ".join(keywords), 60, y, width - 100)
        y -= 10

    # Footer
    y -= 30
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.gray)
    c.drawCentredString(width / 2, 30, "Generated by HireLens ATS Resume Analyzer | hirelens.ai")

    c.save()
    return pdf_path
