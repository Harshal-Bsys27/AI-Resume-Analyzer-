import { useState } from "react";
import { analyzeResume } from "../services/api";

function ResumeUpload({ onResult }) {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!resume || !jobDescription) {
      setError("Please upload resume and enter job description");
      return;
    }

    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      const data = await analyzeResume(formData);
      onResult(data.analysis);
    } catch (err) {
      setError("Failed to analyze resume");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "auto" }}>
      <h2>Upload Resume</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setResume(e.target.files[0])}
        />

        <textarea
          placeholder="Paste Job Description here..."
          rows="8"
          style={{ width: "100%", marginTop: "15px" }}
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button
          type="submit"
          style={{ marginTop: "15px", padding: "10px 20px" }}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {error && <p style={{ color: "red" }}>{error}</p>}
      </form>
    </div>
  );
}

export default ResumeUpload;
