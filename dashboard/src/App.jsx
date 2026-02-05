import { useEffect, useState } from "react";
import { getStatus } from "./services/api";

import CameraView from "./components/CameraView";
import StatusPanel from "./components/StatusPanel";
import ModeControl from "./components/ModeControl";
import ManualControl from "./components/ManualControl";

export default function App() {
  const [status, setStatus] = useState(null);

  useEffect(() => {
    const interval = setInterval(async () => {
      const data = await getStatus();
      setStatus(data);
    }, 800);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app">
      <div className="header panel">🤖 RoboCar Dashboard</div>

      {/* ONE BIG COCKPIT */}
      <div className="panel main-shell">
        <div className="dashboard-grid">
          <div className="camera-box panel">
            <CameraView />
          </div>

          <div className="status-box panel">
            <StatusPanel status={status} />
            <ModeControl currentMode={status?.mode} />
          </div>

          <div className="manual-box panel">
            <ManualControl enabled={status?.mode === "MANUAL"} />
          </div>

          {/* <div className="vision-box panel">
            <StatusPanel status={status} />
          </div> */}
        </div>
      </div>
    </div>
  );
}
