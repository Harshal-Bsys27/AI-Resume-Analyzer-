# HireLens AI Resume Analyzer

**AI-powered ATS Resume Analyzer**  
Simulate how real Applicant Tracking Systems scan, filter, and score your resume. Get actionable feedback, keyword gaps, and role-based insights to improve your chances before you apply.

---

## Features

- **PDF Resume Upload:** Upload your resume in PDF format.
- **Role & JD Matching:** Select a target role or paste a job description for best accuracy.
- **AI Analysis:** Extracts skills, soft skills, certifications, and matches them to the role/JD.
- **ATS Score:** See your overall ATS score and detailed breakdown (skills, experience, education).
- **Skill Tags:** Instantly see matched, missing, and extra skills.
- **Strengths & Weaknesses:** Get personalized strengths, weaknesses, and improvement suggestions.
- **Role-Specific Insights:** View key responsibilities and keywords for your target role.
- **Downloadable PDF Report:** Download a detailed, human-readable report.
- **Modern UI:** Built with React, Tailwind CSS, and Recharts for a clean, interactive experience.
- **No Login Required:** Open to use, no authentication needed.

---

## Tech Stack

- **Frontend:** React, Tailwind CSS, Recharts, Vite
- **Backend:** Flask, Python, PyPDF2, Sentence Transformers, ReportLab
- **AI/NLP:** Sentence Transformers for semantic similarity, custom skill extraction
- **PDF Parsing:** PyPDF2
- **PDF Report Generation:** ReportLab

---


## 🚀 Deploying on Render (Monorepo: Frontend + Backend)

This project is ready for deployment on Render as a single web service. The backend (Flask) serves the built frontend (React) from `backend/frontend_dist`.

**Steps:**
1. Push your code to GitHub.
2. Connect your repo to Render and select the root directory.
3. Render will use the `render.yaml` to build and run both frontend and backend together.
4. All frontend routes and static files are handled by Flask; API endpoints remain accessible.

**Note:**
- The frontend is built to `backend/frontend_dist` and served by Flask.
- For client-side routing (SPA), Flask serves `index.html` for unknown routes.
- Make sure `gunicorn` is in `requirements.txt` (already added).

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Harshal-Bsys27/AI-Resume-Analyzer-Hirelens.git
cd AI-Resume-Analyzer-Hirelens
```

### 2. Backend Setup

- Create a virtual environment and activate it:

  ```bash
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  ```

- Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

- Download the sentence-transformers model (first run will auto-download).

- Start the backend server:

  ```bash
  cd backend
  python app.py
  ```

  The backend runs on `http://127.0.0.1:5000/`

### 3. Frontend Setup

- Install dependencies:

  ```bash
  cd frontend
  npm install
  ```

- Start the frontend dev server:

  ```bash
  npm run dev
  ```

  The frontend runs on `http://localhost:5173/` (or as shown in your terminal).

---

## Usage

1. Go to the frontend URL in your browser.
2. Upload your resume (PDF).
3. Select a target role or paste a job description.
4. Click "Run ATS Analysis".
5. View your ATS score, skill tags, strengths/weaknesses, and download the PDF report.

---

## Deployment

- **Backend:** Deploy Flask app using Gunicorn + Nginx, or use Render/Railway/Heroku.
- **Frontend:** Deploy the built frontend (`npm run build`) to Vercel, Netlify, or any static host.
- **No database required** for open usage.

---

## Customization

- Add more roles, skills, or keywords in `backend/utils/skills.py`.
- Adjust scoring logic in `backend/services/nlp_analyzer.py`.
- Tweak frontend UI in `frontend/src/components/`.

---

## License

MIT License

---

## Credits

- Built by [Harshal-Bsys27](https://github.com/Harshal-Bsys27)
- Powered by OpenAI, HuggingFace, and the open-source community.

---
