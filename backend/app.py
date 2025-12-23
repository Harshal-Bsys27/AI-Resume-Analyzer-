from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

from services.pdf_extractor import extract_text_from_pdf
from services.nlp_analyzer import analyze_resume
from services.report_generator import generate_report_pdf

app = Flask(__name__)
CORS(app)

# ---------------- Output Folder ----------------
OUTPUT_FOLDER = "../output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------- API Route ----------------
@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    jd = request.form.get("job_description")

    if not resume or not jd:
        return jsonify({"error": "Resume or Job Description missing"}), 400

    resume_text = extract_text_from_pdf(resume)
    analysis_result = analyze_resume(resume_text, jd)

    pdf_path = generate_report_pdf(
        analysis_result,
        output_dir=OUTPUT_FOLDER
    )

    return jsonify({
        "status": "success",
        "analysis": analysis_result,
        "pdf_report": pdf_path
    })


@app.route("/download-report", methods=["GET"])
def download_report():
    file_path = request.args.get("path")
    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(file_path, as_attachment=True)


# ---------------- Run Server ----------------
if __name__ == "__main__":
    app.run(debug=True)
