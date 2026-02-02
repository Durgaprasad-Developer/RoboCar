// dashboard/src/components/StatusPanel.jsx

export default function StatusPanel({ status }) {
  if (!status) return <div>Loading status…</div>;

  return (
    <div className="panel">
      <h2>Status</h2>
      <p><b>Mode:</b> {status.mode}</p>
      <p><b>Safety:</b> {status.safety}</p>
      <p><b>Intent:</b> {status.intent}</p>
      <p><b>Motion:</b> {status.motion}</p>

      <h3>Distances</h3>
      <p>Front: {status.distances.front}</p>
      <p>Left: {status.distances.left}</p>
      <p>Right: {status.distances.right}</p>
    </div>
  );
  
}
