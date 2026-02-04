// dashboard/src/services/api.js

const BASE_URL = "http://localhost:8000";

export async function getStatus() {
  const res = await fetch(`${BASE_URL}/status`);
  return res.json();
}

export async function setMode(mode) {
  await fetch(`${BASE_URL}/mode`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mode }),
  });
}

export async function sendManualCommand(command) {
  await fetch(`${BASE_URL}/manual`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ command }),
  });
}

export const VIDEO_URL = `${BASE_URL}/video_feed`;
