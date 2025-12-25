function SkillsTags({ skills }) {
  if (!skills) return null;
  return (
    <div className="flex flex-wrap gap-2 my-2">
      {skills.matched_skills?.map((skill, i) => (
        <span key={"m"+i} className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">{skill}</span>
      ))}
      {skills.missing_skills?.map((skill, i) => (
        <span key={"mi"+i} className="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm">{skill}</span>
      ))}
      {skills.extra_skills?.map((skill, i) => (
        <span key={"e"+i} className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm">{skill}</span>
      ))}
    </div>
  );
}
export default SkillsTags;
