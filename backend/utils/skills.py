# backend/utils/skills.py

import re

GENERAL_SKILLS = [
    # Add a broad set of common technical skills for all roles
    "python", "java", "c++", "c#", "javascript", "typescript", "html", "css", "sql", "mongodb",
    "node", "node.js", "express", "django", "flask", "react", "angular", "vue", "next.js",
    "api", "rest", "graphql", "docker", "kubernetes", "aws", "azure", "gcp", "cloud",
    "linux", "git", "oop", "unit testing", "integration testing", "ci/cd", "microservices",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "machine learning",
    "deep learning", "nlp", "data analysis", "data visualization", "matplotlib", "seaborn",
    "feature engineering", "data mining", "big data", "spark", "hadoop", "data wrangling",
    "data preprocessing", "regression", "classification", "clustering", "model deployment",
    "mlops", "cloudformation", "terraform", "ansible", "jenkins", "prometheus", "grafana",
    "bash", "shell scripting", "firebase", "swift", "objective-c", "android", "ios",
    "xcode", "android studio", "material ui", "bootstrap", "sass", "tailwind", "redux",
    "state management", "webpack", "babel", "figma", "adobe xd", "jira", "scrum", "agile"
]

SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "problem solving", "adaptability",
    "creativity", "critical thinking", "time management", "collaboration",
    "attention to detail", "organization", "work ethic", "interpersonal skills",
    "decision making", "conflict resolution", "empathy", "initiative", "flexibility"
]

CERTIFICATIONS = [
    "aws certified", "azure certified", "gcp certified", "pmp", "scrum master",
    "oracle certified", "microsoft certified", "google certified", "ccna", "ocp",
    "cissp", "comptia", "data science certification", "machine learning certification",
    "react certification", "python certification", "java certification"
]

ROLE_SKILLS = {
    "data scientist": [
        "python", "pandas", "numpy", "machine learning", "deep learning",
        "statistics", "sql", "tensorflow", "pytorch", "data visualization",
        "scikit-learn", "matplotlib", "seaborn", "data mining", "feature engineering",
        "jupyter", "spark", "hadoop", "big data", "data wrangling", "data preprocessing",
        "regression", "classification", "clustering", "nlp", "natural language processing",
        "model deployment", "mlops", "cloud", "aws", "azure", "gcp"
    ],
    "backend developer": [
        "python", "java", "node", "node.js", "flask", "django", "api", "sql", "mongodb",
        "docker", "aws", "microservices", "rest", "graphql", "postgresql", "redis",
        "spring", "express", "oop", "oop concepts", "unit testing", "integration testing",
        "linux", "nginx", "c#", ".net", "kafka", "rabbitmq", "ci/cd", "azure", "gcp"
    ],
    "frontend developer": [
        "html", "css", "javascript", "react", "tailwind", "ui", "ux",
        "responsive design", "redux", "typescript", "next.js", "vue", "sass",
        "bootstrap", "material ui", "webpack", "babel", "figma", "adobe xd",
        "cross-browser", "accessibility", "testing library", "jest", "cypress"
    ],
    "ai engineer": [
        "machine learning", "deep learning", "nlp", "opencv", "tensorflow",
        "pytorch", "python", "model deployment", "mlops", "huggingface",
        "transformers", "bert", "gpt", "computer vision", "speech recognition",
        "reinforcement learning", "cloud", "aws", "azure", "gcp"
    ],
    "full stack developer": [
        "javascript", "react", "node", "express", "mongodb", "sql", "python",
        "django", "flask", "html", "css", "aws", "docker", "typescript",
        "graphql", "rest", "redux", "sass", "unit testing", "ci/cd", "azure", "gcp"
    ],
    "devops engineer": [
        "docker", "kubernetes", "aws", "azure", "ci/cd", "jenkins", "linux",
        "terraform", "ansible", "monitoring", "prometheus", "grafana",
        "cloudformation", "gcp", "scripting", "bash", "python", "helm", "gitlab ci"
    ],
    "product manager": [
        "roadmap", "agile", "scrum", "stakeholder", "user stories", "jira",
        "market research", "product strategy", "ux", "analytics", "a/b testing",
        "wireframing", "prototyping", "kpi", "go-to-market", "requirements gathering"
    ],
    "data analyst": [
        "sql", "excel", "tableau", "power bi", "python", "data visualization",
        "statistics", "data cleaning", "reporting", "dashboards", "business intelligence",
        "data mining", "pivot tables", "vba", "access", "r", "lookml", "qlik"
    ],
    "machine learning engineer": [
        "python", "machine learning", "deep learning", "tensorflow", "pytorch",
        "model deployment", "mlops", "feature engineering", "scikit-learn",
        "cloud", "aws", "azure", "gcp", "docker", "kubernetes", "data pipelines"
    ],
    "android developer": [
        "java", "kotlin", "android studio", "xml", "jetpack", "firebase",
        "mvvm", "retrofit", "dagger", "material design", "unit testing", "gradle"
    ],
    "ios developer": [
        "swift", "objective-c", "xcode", "cocoa", "cocoapods", "swiftui",
        "core data", "mvvm", "alamofire", "autolayout", "unit testing"
    ]
}

ROLE_RESPONSIBILITIES = {
    "data scientist": [
        "Build and deploy machine learning models",
        "Data cleaning and preprocessing",
        "Statistical analysis and hypothesis testing",
        "Data visualization and reporting",
        "Feature engineering and selection",
        "Collaborate with cross-functional teams to solve business problems",
        "Communicate findings to stakeholders"
    ],
    "backend developer": [
        "Design and implement RESTful APIs",
        "Database schema design and optimization",
        "Server-side logic and integration",
        "Unit and integration testing",
        "Cloud deployment and scaling",
        "Maintain and improve backend performance",
        "Ensure security and data protection"
    ],
    "frontend developer": [
        "Develop responsive web interfaces",
        "Implement UI/UX designs",
        "Cross-browser compatibility",
        "State management (Redux, Context API)",
        "Accessibility and performance optimization",
        "Collaborate with designers and backend developers",
        "Maintain code quality and best practices"
    ],
    "ai engineer": [
        "Develop and deploy AI models",
        "Research and implement new AI algorithms",
        "Optimize model performance",
        "Integrate AI solutions into products",
        "Collaborate with data scientists and engineers"
    ],
    "full stack developer": [
        "Develop both frontend and backend components",
        "Integrate APIs and databases",
        "Ensure application scalability and performance",
        "Collaborate with cross-functional teams",
        "Maintain code quality and documentation"
    ],
    "devops engineer": [
        "Automate CI/CD pipelines",
        "Manage cloud infrastructure",
        "Monitor and optimize system performance",
        "Ensure security and compliance",
        "Collaborate with development teams"
    ],
    "product manager": [
        "Define product vision and strategy",
        "Gather and prioritize requirements",
        "Coordinate with engineering, design, and marketing",
        "Monitor product performance and KPIs",
        "Lead product launches and iterations"
    ],
    "data analyst": [
        "Analyze and interpret complex data sets",
        "Create dashboards and reports",
        "Identify trends and insights",
        "Collaborate with business stakeholders",
        "Support data-driven decision making"
    ],
    "machine learning engineer": [
        "Design and implement ML algorithms",
        "Build scalable ML pipelines",
        "Deploy and monitor models in production",
        "Collaborate with data scientists and engineers",
        "Optimize model performance"
    ],
    "android developer": [
        "Develop Android applications",
        "Integrate APIs and third-party libraries",
        "Ensure app performance and security",
        "Collaborate with designers and backend developers",
        "Maintain code quality and documentation"
    ],
    "ios developer": [
        "Develop iOS applications",
        "Integrate APIs and third-party libraries",
        "Ensure app performance and security",
        "Collaborate with designers and backend developers",
        "Maintain code quality and documentation"
    ],
    "general": [
        "Refer to the job description for responsibilities."
    ]
}

ROLE_KEYWORDS = {
    "data scientist": [
        "machine learning", "data analysis", "python", "statistics", "model deployment", "data visualization", "feature engineering", "big data", "predictive modeling"
    ],
    "backend developer": [
        "api", "database", "server", "python", "java", "node.js", "sql", "microservices", "cloud", "docker"
    ],
    "frontend developer": [
        "react", "javascript", "html", "css", "ui", "ux", "responsive", "redux", "typescript", "web"
    ],
    "ai engineer": [
        "ai", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch", "model optimization", "deployment"
    ],
    "full stack developer": [
        "frontend", "backend", "api", "database", "react", "node.js", "python", "full stack", "cloud"
    ],
    "devops engineer": [
        "ci/cd", "automation", "cloud", "docker", "kubernetes", "infrastructure", "monitoring", "deployment"
    ],
    "product manager": [
        "product strategy", "roadmap", "requirements", "stakeholder", "kpi", "launch", "market research"
    ],
    "data analyst": [
        "data analysis", "sql", "excel", "dashboard", "reporting", "visualization", "business intelligence"
    ],
    "machine learning engineer": [
        "machine learning", "model deployment", "mlops", "python", "pipeline", "cloud", "tensorflow", "pytorch"
    ],
    "android developer": [
        "android", "java", "kotlin", "mobile", "app", "ui", "api", "firebase"
    ],
    "ios developer": [
        "ios", "swift", "objective-c", "mobile", "app", "ui", "api", "xcode"
    ],
    "general": [
        "Refer to the job description for keywords."
    ]
}

ROLE_ALIASES = {
    "software development engineer": "full stack developer",
    "sde": "full stack developer",
    "product intern": "product manager",
    "sde 1": "full stack developer",
    "sde 2": "full stack developer",
    "sde 3": "full stack developer",
    "frontend": "frontend developer",
    "backend": "backend developer",
    "ml engineer": "machine learning engineer",
    "data science": "data scientist",
    "data analyst intern": "data analyst",
    "devops": "devops engineer",
    "ai": "ai engineer",
    "full stack": "full stack developer"
}

def infer_role(job_description: str):
    jd = job_description.lower()
    for role in ROLE_SKILLS:
        if role in jd:
            return role
    # Fallback: keyword match
    for role, skills in ROLE_SKILLS.items():
        for skill in skills:
            if skill in jd:
                return role
    return "general"

def extract_skills(text: str):
    text = text.lower()
    found = set()
    for skill in GENERAL_SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.add(skill)
    return list(found)

def extract_soft_skills(text: str):
    text = text.lower()
    found = set()
    for skill in SOFT_SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.add(skill)
    return list(found)

def extract_certifications(text: str):
    text = text.lower()
    found = set()
    for cert in CERTIFICATIONS:
        if cert in text:
            found.add(cert)
    return list(found)

def canonical_role(role: str):
    if not role:
        return "general"
    role = role.strip().lower()
    return ROLE_ALIASES.get(role, role)

def get_role_responsibilities(role: str):
    role = canonical_role(role)
    if role in ROLE_RESPONSIBILITIES and ROLE_RESPONSIBILITIES[role]:
        return ROLE_RESPONSIBILITIES[role]
    # Generic fallback (not just a string)
    return [
        "Review the job description for specific responsibilities.",
        "Highlight your achievements and impact in previous roles.",
        "Demonstrate your ability to work in teams and solve problems."
    ]

def get_role_keywords(role: str):
    role = canonical_role(role)
    if role in ROLE_KEYWORDS and ROLE_KEYWORDS[role]:
        return ROLE_KEYWORDS[role]
    # Generic fallback (not just a string)
    return [
        "teamwork", "communication", "problem solving", "leadership", "project management",
        "collaboration", "initiative", "adaptability", "technical skills", "results"
    ]
