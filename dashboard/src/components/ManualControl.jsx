// dashboard/src/components/ManualControl.jsx

import { useState } from "react";
import { sendManualCommand } from "../services/api";

const COMMANDS = ["FORWARD", "LEFT", "RIGHT", "BACK", "STOP"];

export default function ManualControl({ enabled }) {
  const [activeCmd, setActiveCmd] = useState(null);

  const handleClick = (cmd) => {
    sendManualCommand(cmd);

    if (cmd === "STOP") {
      setActiveCmd(null);
    } else {
      setActiveCmd(cmd);
    }
  };

  return (
    <>
      <h2>Manual Control</h2>

      {!enabled && <p className="hint">Switch to MANUAL mode</p>}

      <div className="manual-buttons">
        {COMMANDS.map((cmd) => (
          <button
            key={cmd}
            disabled={!enabled}
            onClick={() => handleClick(cmd)}
            className={activeCmd === cmd ? "manual-active" : ""}
          >
            {cmd}
          </button>
        ))}
      </div>
    </>
  );
}


