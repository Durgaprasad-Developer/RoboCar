// dashboard/src/component/statusPanel.jsx

export default function StatusPanel({ status }) {
  if (!status) return <div className="panel">Loading status…</div>;

  // 🔑 FIX: ball data comes from `status.perception`
  const ball = status.perception;

  return (
    <div className="panel">
      <h2>Status</h2>

      <p><b>Mode:</b> {status.mode}</p>
      <p><b>Safety:</b> {status.safety}</p>
      <p><b>Intent:</b> {status.intent}</p>
      <p><b>Motion:</b> {status.motion}</p>

      <h3>Distances</h3>
      <p>Front: {status.distances?.front ?? "-"}</p>
      <p>Left: {status.distances?.left ?? "-"}</p>
      <p>Right: {status.distances?.right ?? "-"}</p>

      {/* 🔥 BALL TRACKING UI */}
      {status.mode === "TRACK_BALL" && (
        <>
          <h3>Ball Tracking</h3>
          <p>
            Seen: {ball?.ball_seen ? "YES" : "NO"}
          </p>
          <p>
            Position: {ball?.ball_position ?? "NONE"}
          </p>
        </>
      )}
    </div>
  );
}
