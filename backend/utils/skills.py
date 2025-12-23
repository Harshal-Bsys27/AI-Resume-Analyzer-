# backend/utils/skills.py

SKILLS_DB = [
    "python", "java", "c++", "flask", "django", "react", "node",
    "sql", "mongodb", "machine learning", "deep learning",
    "nlp", "opencv", "data analysis", "tensorflow", "pytorch",
    "aws", "docker", "git", "linux"
]

def extract_skills(text):
    found_skills = set()
    text = text.lower()

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)
