// dashboard/src/components/StatusPanel.jsx

export default function StatusPanel({ status }) {
  if (!status) return <div className="panel">Loading status…</div>;

  const perception = status.perception || {};

  return (
    <div className="panel">
      <h2>Status</h2>

      <p><b>Mode:</b> {status.mode}</p>
      <p><b>Safety:</b> {status.safety}</p>
      <p><b>Intent:</b> {status.intent}</p>
      <p><b>Motion:</b> {status.motion}</p>

      <h3>Distances</h3>
      <p>Front: {status.distances?.front}</p>
      <p>Left: {status.distances?.left}</p>
      <p>Right: {status.distances?.right}</p>

      {status.mode === "TRACK_BALL" && (
        <>
          <h3>Ball Tracking</h3>
          <p>Seen: {perception.ball_seen ? "YES" : "NO"}</p>
          <p>Position: {perception.ball_position || "NONE"}</p>
        </>
      )}

      {status.mode === "FOLLOW_OWNER" && (
  <>
    <h3>Face Recognition</h3>

    {status.perception.owner_status === "OWNER" && (
      <p style={{ color: "#22c55e" }}>OWNER DETECTED ✅</p>
    )}

    {status.perception.owner_status === "UNKNOWN" && (
      <p style={{ color: "#ef4444" }}>UNKNOWN PERSON ❌</p>
    )}

    {status.perception.owner_status === "NONE" && (
      <p>No face detected</p>
    )}
  </>
)}

{status.mode === "DETECT_OBJECT" && (
  <>
    <h3>Object Detection</h3>

    {status.perception.objects.length === 0 && (
      <p>No objects detected</p>
    )}

    <ul>
      {status.perception.objects.map((obj, i) => (
        <li key={i}>{obj}</li>
      ))}
    </ul>
  </>
)}


    </div>
  );
}
