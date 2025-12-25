function Scorecard({ overall, breakdown }) {
  return (
    <div className="flex flex-col md:flex-row gap-6 my-4">
      <div className="bg-white border rounded-xl p-6 flex-1 text-center">
        <div className="text-4xl font-bold text-orange-600">{overall}%</div>
        <div className="text-gray-600 mt-2">Overall ATS Score</div>
      </div>
      <div className="bg-white border rounded-xl p-6 flex-1">
        <div className="font-semibold mb-2 text-orange-700">Score Breakdown</div>
        <ul className="text-gray-700 space-y-1">
          <li>Skills Match: <span className="font-bold">{breakdown.skills_match}%</span></li>
          <li>Experience Match: <span className="font-bold">{breakdown.experience_match}%</span></li>
          <li>Education Match: <span className="font-bold">{breakdown.education_match}%</span></li>
        </ul>
      </div>
    </div>
  );
}
export default Scorecard;
