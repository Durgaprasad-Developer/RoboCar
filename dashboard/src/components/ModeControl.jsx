// dashboard/src/components/ModeControl.jsx

import { setMode } from "../services/api";

const MODES = ["IDLE", "AUTO", "MANUAL", "TRACK_BALL"];

export default function ModeControl({ currentMode }) {
  return (
    <div className="panel">
      <h2>Mode Control</h2>

      {MODES.map((mode) => (
        <button
          key={mode}
          onClick={() => setMode(mode)}
          className={currentMode === mode ? "active" : ""}
        >
          {mode}
        </button>
      ))}
    </div>
  );
}
