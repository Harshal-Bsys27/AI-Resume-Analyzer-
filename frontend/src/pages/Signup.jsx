import { useState } from "react";

function Signup({ onSignup }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");
  const [msg, setMsg] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSignup(e) {
    e.preventDefault();
    setLoading(true);
    setErr("");
    setMsg("");
    try {
      const res = await fetch("http://127.0.0.1:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await res.json();
      if (res.ok) {
        setMsg("Signup successful! You can now login.");
        setEmail("");
        setPassword("");
        if (onSignup) onSignup(data);
      } else {
        setErr(data.error || "Signup failed");
      }
    } catch {
      setErr("Network error");
    }
    setLoading(false);
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-50 to-gray-100">
      <form
        onSubmit={handleSignup}
        className="bg-white rounded-xl shadow-xl p-8 w-full max-w-md border"
      >
        <h2 className="text-2xl font-bold mb-6 text-orange-700">Sign Up</h2>
        <input
          type="email"
          className="w-full mb-4 px-4 py-2 border rounded"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          className="w-full mb-4 px-4 py-2 border rounded"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        <button
          type="submit"
          className="w-full bg-orange-600 text-white py-2 rounded font-semibold hover:bg-orange-700 transition"
          disabled={loading}
        >
          {loading ? "Signing up..." : "Sign Up"}
        </button>
        {err && <div className="text-red-600 mt-3 text-center">{err}</div>}
        {msg && <div className="text-green-600 mt-3 text-center">{msg}</div>}
      </form>
    </div>
  );
}

export default Signup;
