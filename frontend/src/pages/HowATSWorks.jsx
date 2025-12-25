import React from "react";
import Navbar from "../components/navbar";

function HowATSWorks() {
  return (
    <>
      <Navbar />
      <div className="max-w-3xl mx-auto py-16 px-6 text-gray-800">
        <h1 className="text-4xl font-bold text-amber-700 mb-6">How Our ATS Resume Analyzer Works</h1>
        <p className="mb-6 text-lg text-gray-700">
          HireLens helps you optimize your resume for real-world Applicant Tracking Systems (ATS) used by employers. Our analyzer gives you actionable feedback so you can stand out and get noticed.
        </p>
        <h2 className="text-2xl font-semibold text-amber-600 mt-8 mb-3">What is an ATS?</h2>
        <ul className="list-disc list-inside mb-6 text-gray-700">
          <li>ATS software automatically screens resumes for keywords, skills, and experience.</li>
          <li>It ranks and filters candidates based on how well their resume matches the job requirements.</li>
          <li>Many resumes are rejected if they lack the right keywords or structure.</li>
        </ul>
        <h2 className="text-2xl font-semibold text-amber-600 mt-8 mb-3">How Does HireLens Work?</h2>
        <ol className="list-decimal list-inside mb-6 text-gray-700 space-y-2">
          <li><b>Upload your Resume:</b> We extract text from your PDF resume using advanced parsing.</li>
          <li><b>Paste Job Description or Select Role:</b> We analyze the job description or infer the role.</li>
          <li><b>Keyword & Skill Matching:</b> Our AI matches your resume's skills, experience, and certifications against the job requirements and role standards.</li>
          <li><b>Soft Skills & Certifications:</b> We check for soft skills and relevant certifications.</li>
          <li><b>Scoring & Suggestions:</b> Your resume is scored and you get strengths, weaknesses, and improvement tips.</li>
          <li><b>Downloadable Report:</b> Save a professional PDF report for your records.</li>
        </ol>
        <h2 className="text-2xl font-semibold text-amber-600 mt-8 mb-3">Tips for Beating the ATS</h2>
        <ul className="list-disc list-inside mb-6 text-gray-700">
          <li>Use standard section headings (e.g., "Experience", "Education", "Skills").</li>
          <li>Include keywords from the job description naturally.</li>
          <li>List both technical and soft skills relevant to the role.</li>
          <li>Quantify your achievements with numbers and results.</li>
          <li>Keep formatting simple and avoid images or tables.</li>
          <li>Save your resume as a PDF for best compatibility.</li>
        </ul>
        <div className="mt-10 text-center">
          <a
            href="/"
            className="inline-block px-6 py-3 rounded-xl bg-amber-700 text-white font-semibold hover:bg-amber-800 transition"
          >
            Back to Resume Analyzer
          </a>
        </div>
      </div>
    </>
  );
}

export default HowATSWorks;
