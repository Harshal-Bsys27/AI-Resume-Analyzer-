const API_BASE = "http://127.0.0.1:5000";

export async function analyzeResume(formData) {
  try {
    const response = await fetch(`${API_BASE}/analyze`, {
      method: "POST",
      body: formData,
    });

    // ❌ Backend error handling
    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(errorText || "Backend error");
    }

    // ✅ Successful response
    const data = await response.json();
    return data;

  } catch (error) {
    console.error("API ERROR:", error);
    throw error; // important: frontend catch will handle this
  }
}
