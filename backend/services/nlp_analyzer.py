import re
from utils.skills import extract_skills

# ---------------- Helpers ----------------
def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def detect_fresher(resume_text):
    fresher_keywords = [
        "fresher", "student", "intern", "internship",
        "final year", "undergraduate", "graduate"
    ]
    return any(word in resume_text for word in fresher_keywords)


def has_degree(resume_text):
    degree_keywords = [
        "bachelor", "b.tech", "b.e", "bsc",
        "master", "m.tech", "msc", "mba", "phd"
    ]
    return any(word in resume_text for word in degree_keywords)


# ---------------- Main Analyzer ----------------
def analyze_resume(resume_text, jd_text):
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    # ---------------- SKILLS SCORE (50%) ----------------
    if jd_skills:
        skills_score = (len(matched_skills) / len(jd_skills)) * 100
    else:
        skills_score = 50.0

    # ---------------- EXPERIENCE SCORE (30%) ----------------
    is_fresher = detect_fresher(resume_text)

    if is_fresher:
        # ATS does not punish freshers
        experience_score = 65.0
    else:
        experience_score = min(90.0, skills_score + 10)

    # ---------------- EDUCATION SCORE (20%) ----------------
    education_score = 70.0

    if has_degree(resume_text):
        education_score = 85.0
    else:
        education_score = 55.0

    # ---------------- FINAL ATS SCORE ----------------
    overall_score = (
        (skills_score * 0.5) +
        (experience_score * 0.3) +
        (education_score * 0.2)
    )

    # ---------------- Feedback ----------------
    strengths = []
    weaknesses = []

    if skills_score >= 70:
        strengths.append("Good skill keyword alignment with job description")
    else:
        weaknesses.append("Low skill match based on job keywords")

    if is_fresher:
        strengths.append("Fresher profile evaluated without experience penalty")
    elif experience_score < 60:
        weaknesses.append("Experience section lacks role-specific keywords")

    if missing_skills:
        weaknesses.append(
            f"Missing key skills: {', '.join(missing_skills)}"
        )

    suggestions = [
        "Reuse job description keywords naturally in resume",
        "Add project descriptions aligned with job role",
        "Explicitly list tools, technologies, and frameworks"
    ]

    return {
        "overall_score": round(float(overall_score), 2),
        "profile_type": "Fresher" if is_fresher else "Experienced",
        "score_breakdown": {
            "skills_match": round(float(skills_score), 2),
            "experience_match": round(float(experience_score), 2),
            "education_match": round(float(education_score), 2)
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
