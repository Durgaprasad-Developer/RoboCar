// dashboard/src/components/ModeControl.jsx

import { setMode } from "../services/api";

const MODES = [
  "IDLE",
  "AUTO",
  "MANUAL",
  "TRACK_BALL",
  "FOLLOW_OWNER",
  "DETECT_OBJECT",
];

export default function ModeControl({ currentMode }) {
  return (
    <>
      <h2>Mode Control</h2>

      <div className="mode-buttons">
        {MODES.map((mode) => (
          <button
            key={mode}
            className={currentMode === mode ? "active" : ""}
            onClick={() => setMode(mode)}
          >
            {mode}
          </button>
        ))}
      </div>
    </>
  );
}
