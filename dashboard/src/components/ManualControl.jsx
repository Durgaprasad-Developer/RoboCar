// dashboard/src/components/ManualControl.jsx

import { sendManualCommand } from "../services/api";

const COMMANDS = ["FORWARD", "LEFT", "RIGHT", "BACK", "STOP"];

export default function ManualControl({ enabled }) {
  return (
    <div className="panel">
      <h2>Manual Control</h2>

      {!enabled && <p>Switch to MANUAL mode</p>}

      {COMMANDS.map((cmd) => (
        <button
          key={cmd}
          disabled={!enabled}
          onClick={() => sendManualCommand(cmd)}
        >
          {cmd}
        </button>
      ))}
    </div>
  );
}
