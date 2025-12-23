import { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import AnalysisResult from "./components/AnalysisResult";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1 style={{ textAlign: "center" }}>AI Resume Analyzer</h1>

      <ResumeUpload onResult={setResult} />
      <AnalysisResult data={result} />
    </div>
  );
}

export default App;
