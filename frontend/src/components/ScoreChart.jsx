import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";

function ScoreChart({ chartData }) {
  if (!chartData) return null;
  // Convert chartData object to array for recharts
  const data = Object.entries(chartData).map(([name, value]) => ({ name, value }));

  return (
    <div className="bg-white border rounded-xl p-6 my-4">
      <div className="font-semibold mb-2 text-orange-700">Score Chart</div>
      <ResponsiveContainer width="100%" height={220}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" fontSize={12} />
          <YAxis domain={[0, 100]} />
          <Tooltip />
          <Bar dataKey="value" fill="#fb923c" radius={[6, 6, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
export default ScoreChart;
