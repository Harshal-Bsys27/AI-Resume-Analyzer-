const API_BASE = "http://127.0.0.1:5000";

export async function analyzeResume(formData) {
  const response = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    body: formData
  });

  return response.json();
}
