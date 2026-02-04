// dashboard/src/components/CameraView.jsx

import { VIDEO_URL } from "../services/api";

export default function CameraView() {
  return (
    <div className="panel">
      <h2>Camera</h2>
      <img
        src={VIDEO_URL}
        alt="RoboCar Camera"
        style={{
          width: "100%",
          borderRadius: "8px",
          border: "2px solid #334155",
        }}
      />
    </div>
  );
}
