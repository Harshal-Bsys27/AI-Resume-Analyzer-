import { useState } from "react";
import { analyzeResume } from "../services/api";

const ROLES = [
  "Software Development Engineer",
  "Frontend Developer",
  "Backend Developer",
  "Full Stack Developer",
  "Data Scientist",
  "Data Analyst",
  "Machine Learning Engineer",
  "DevOps Engineer",
  "Product Intern",
];

function ResumeUpload({ onResult }) {
  const [resume, setResume] = useState(null);
  const [role, setRole] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!resume) {
      setError("Please upload your resume");
      onResult(null);
      return;
    }

    if (!role && !jobDescription) {
      setError("Select a role or provide a job description");
      onResult(null);
      return;
    }

    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription || role);
    formData.append("role", role);

    try {
      const data = await analyzeResume(formData);

      if (data?.analysis) {
        setError("");
        onResult({ ...data.analysis, download_url: data.download_url });
      } else if (data?.error) {
        setError(data.error);
        onResult(null);
      } else {
        setError("No analysis result received.");
        onResult(null);
      }
    } catch {
      setError("Resume analysis failed. Try again.");
      onResult(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white border border-blue-100 rounded-3xl shadow-xl w-full max-w-5xl mx-auto overflow-visible">
      <div className="flex flex-col md:flex-row">
        {/* LEFT PANEL */}
        <div className="md:w-1/3 bg-orange-50 px-10 py-14 flex flex-col justify-center">
          <div className="bg-white rounded-full p-5 mb-6 shadow-sm w-fit">
            <svg
              className="w-14 h-14 text-orange-600"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              viewBox="0 0 48 48"
            >
              <rect x="8" y="8" width="32" height="35" rx="6" />
              <path d="M16 20h16M16 28h10" strokeLinecap="round" />
            </svg>
          </div>

          <h2 className="text-3xl font-bold text-gray-900 mb-3">
            Upload your Resume
          </h2>
          <p className="text-gray-600 text-base leading-relaxed">
            Get ATS compatibility score, keyword gaps, and role-based insights
            tailored to your resume.
          </p>
        </div>

        {/* RIGHT PANEL */}
        <div className="md:w-2/3 px-6 sm:px-10 py-12">
          <form onSubmit={handleSubmit} className="space-y-8 w-full">
            {/* Resume */}
            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Resume (PDF)
              </label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => setResume(e.target.files[0])}
                className="w-full border border-gray-300 rounded-xl px-4 py-3 text-sm bg-gray-50"
              />
            </div>

            {/* Role */}
            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Target Role (optional)
              </label>
              <select
                value={role}
                onChange={(e) => setRole(e.target.value)}
                className="w-full rounded-xl border border-gray-300 px-4 py-3 text-sm"
              >
                <option value="">Select a role</option>
                {ROLES.map((r, i) => (
                  <option key={i} value={r}>
                    {r}
                  </option>
                ))}
              </select>
            </div>

            {/* JD */}
            <div>
              <label className="block text-sm font-semibold text-gray-700 mb-2">
                Job Description (optional)
              </label>
              <textarea
                rows="5"
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
                className="w-full rounded-xl border border-gray-300 px-4 py-3 text-sm resize-none"
                placeholder="Paste job description for best accuracy"
              />
            </div>

            {/* Submit */}
            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 rounded-xl bg-orange-600 text-white font-semibold hover:bg-blue-700 transition"
            >
              {loading ? "Analyzing..." : "Run ATS Analysis"}
            </button>

            {error && (
              <p className="text-red-600 text-sm text-center">{error}</p>
            )}
          </form>
        </div>
      </div>
    </div>
  );
}

export default ResumeUpload;
