// dashboard/src/components/CameraView.jsx

import { VIDEO_URL } from "../services/api";

export default function CameraView() {
  return (
    <>
      <h2>Camera</h2>
      <img src={VIDEO_URL} alt="Camera Feed" />
    </>
  );
}

