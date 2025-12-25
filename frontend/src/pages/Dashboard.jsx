import { useState } from "react";
import ResumeUpload from "../components/ResumeUpload";
import Scorecard from "../components/Scorecard";
import ScoreChart from "../components/ScoreChart";
import SkillsTags from "../components/SkillsTags";
import AnalysisResult from "../components/AnalysisResult";

// Demo data for initial dashboard view
const DEMO = {
  overall_score: 72,
  score_breakdown: {
    skills_match: 65,
    experience_match: 80,
    education_match: 70,
  },
  chart_data: {
    "Tech Stack Coverage": 60,
    "Skills Match": 65,
    "Experience Match": 80,
    "Education Match": 70,
    "Semantic Similarity": 55,
    "Overall ATS Score": 72,
  },
  skills: {
    matched_skills: ["python", "react", "sql"],
    missing_skills: ["docker", "aws"],
    extra_skills: ["c++"],
  },
};

function Dashboard() {
  const [result, setResult] = useState(null);

  // Use demo data if no result yet
  const scorecardData = result
    ? { overall: result.overall_score, breakdown: result.score_breakdown }
    : { overall: DEMO.overall_score, breakdown: DEMO.score_breakdown };
  const chartData = result ? result.chart_data : DEMO.chart_data;
  const skills = result ? result.skills : DEMO.skills;

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 pb-16">
      <div className="max-w-7xl mx-auto px-6 py-10">
        <h1 className="text-3xl font-bold mb-6 text-orange-700">ATS Dashboard</h1>
        <Scorecard overall={scorecardData.overall} breakdown={scorecardData.breakdown} />
        <ScoreChart chartData={chartData} />
        <div>
          <h3 className="text-xl font-bold mb-2 text-orange-700">Skill Tags</h3>
          <SkillsTags skills={skills} />
        </div>
        <div className="mt-10">
          <ResumeUpload onResult={setResult} />
        </div>
        {!result && (
          <div className="mt-10 text-center text-gray-500 text-lg">
            <p>
              Upload your resume and select a role or paste a job description to see your personalized ATS analysis here.
            </p>
            <p className="mt-2 text-sm text-gray-400">
              (Demo data is shown above until you upload your own resume.)
            </p>
          </div>
        )}
        {result && (
          <div className="mt-10">
            <AnalysisResult data={result} />
          </div>
        )}
      </div>
    </div>
  );
}
export default Dashboard;
