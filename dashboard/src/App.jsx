// dashboard/src/App.jsx

import { useEffect, useState } from "react";
import { getStatus } from "./services/api";

import StatusPanel from "./components/StatusPanel";
import ModeControl from "./components/ModeControl";
import ManualControl from "./components/ManualControl";

export default function App() {
  const [status, setStatus] = useState(null);

  useEffect(() => {
    const interval = setInterval(async () => {
      const data = await getStatus();
      setStatus(data);
    }, 800); // polling every 800 ms

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app">
      <h1>🤖 RoboCar Dashboard</h1>

      <StatusPanel status={status} />

      <ModeControl currentMode={status?.mode} />

      <ManualControl enabled={status?.mode === "MANUAL"} />
    </div>
  );
}
