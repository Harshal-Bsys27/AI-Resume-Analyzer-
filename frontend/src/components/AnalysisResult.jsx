function AnalysisResult({ data }) {
  if (!data) return null;

  return (
    <div style={{ maxWidth: "700px", margin: "40px auto" }}>
      <h2>Analysis Result</h2>

      <h3>Overall Score: {data.overall_score}%</h3>

      <h4>Score Breakdown</h4>
      <ul>
        <li>Skills Match: {data.score_breakdown.skills_match}%</li>
        <li>Experience Match: {data.score_breakdown.experience_match}%</li>
        <li>Education Match: {data.score_breakdown.education_match}%</li>
      </ul>

      <h4>Matched Skills</h4>
      <p>{data.skills.matched_skills.join(", ") || "None"}</p>

      <h4>Missing Skills</h4>
      <p>{data.skills.missing_skills.join(", ") || "None"}</p>

      <h4>Strengths</h4>
      <ul>
        {data.strengths.map((s, i) => (
          <li key={i}>{s}</li>
        ))}
      </ul>

      <h4>Weaknesses</h4>
      <ul>
        {data.weaknesses.map((w, i) => (
          <li key={i}>{w}</li>
        ))}
      </ul>

      <h4>Suggestions</h4>
      <ul>
        {data.suggestions.map((s, i) => (
          <li key={i}>{s}</li>
        ))}
      </ul>
    </div>
  );
}

export default AnalysisResult;
