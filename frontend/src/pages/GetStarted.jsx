import Navbar from "../components/navbar";

function GetStarted() {
  return (
    <>
      <Navbar />
      <div className="max-w-3xl mx-auto py-16 px-6 text-gray-800">
        <h1 className="text-4xl font-bold text-amber-700 mb-6">Get Started with HireLens</h1>
        <p className="mb-6 text-lg text-gray-700">
          Welcome to <b>HireLens</b>! Our ATS Resume Analyzer helps you improve your resume so it passes automated screening and impresses recruiters.
        </p>
        <h2 className="text-2xl font-semibold text-amber-600 mt-8 mb-3">How to Use HireLens</h2>
        <ol className="list-decimal list-inside mb-6 text-gray-700 space-y-2">
          <li><b>Upload your Resume:</b> Select your PDF resume and upload it.</li>
          <li><b>Choose Target Role or Paste Job Description:</b> Select a role or paste the job description for best results.</li>
          <li><b>Run ATS Analysis:</b> Our AI scans your resume and scores it just like a real ATS.</li>
          <li><b>Review Your Report:</b> See strengths, weaknesses, missing skills, and suggestions.</li>
          <li><b>Download PDF Report:</b> Save your analysis as a professional PDF.</li>
        </ol>
        <h2 className="text-2xl font-semibold text-amber-600 mt-8 mb-3">Features</h2>
        <ul className="list-disc list-inside mb-6 text-gray-700">
          <li>Real ATS simulation for resume screening</li>
          <li>Role-based and job description-based analysis</li>
          <li>Skill, tech stack, and soft skill matching</li>
          <li>Actionable improvement suggestions</li>
          <li>Downloadable PDF report</li>
        </ul>
        <div className="mt-10 text-center">
          <a
            href="/"
            className="inline-block px-6 py-3 rounded-xl bg-amber-700 text-white font-semibold hover:bg-amber-800 transition"
          >
            Back to Home
          </a>
        </div>
      </div>
    </>
  );
}

export default GetStarted;
