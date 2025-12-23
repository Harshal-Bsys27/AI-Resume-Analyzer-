import re
from utils.scoring import semantic_similarity
from utils.skills import extract_skills

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()

def analyze_resume(resume_text, jd_text):
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    overall_score = float(semantic_similarity(resume_text, jd_text))

    skills_score = float(
        (len(matched_skills) / max(len(jd_skills), 1)) * 100
    )

    experience_score = float(
        semantic_similarity(resume_text[:1500], jd_text[:1500])
    )

    education_score = 70.0  # force Python float

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
        weaknesses.append(
            f"Missing important skills: {', '.join(missing_skills)}"
        )

    suggestions = [
        "Add quantified achievements in experience section",
        "Include missing skills relevant to the job role",
        "Optimize resume keywords for ATS systems"
    ]

    return {
        "overall_score": overall_score,
        "score_breakdown": {
            "skills_match": skills_score,
            "experience_match": experience_score,
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
