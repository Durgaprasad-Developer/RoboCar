# backeend/api/routes.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
import cv2

from api.schemas import ModeRequest, ManualCommandRequest
from core.state import (
    get_robot_mode,
    set_robot_mode,
    set_manual_command,
    RobotMode,
)
from core.loop import get_last_snapshot
from vision.camera import Camera

router = APIRouter()
_camera: Camera | None = None


def set_camera(camera: Camera):
    global _camera
    _camera = camera


@router.get("/status")
def get_status():
    return get_last_snapshot()


@router.get("/video_feed")
def video_feed():
    def generate():
        while True:
            frame = _camera.get_frame()
            if frame is None:
                continue

            _, jpeg = cv2.imencode(".jpg", frame)
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n"
                + jpeg.tobytes()
                + b"\r\n"
            )

    return StreamingResponse(
        generate(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )


@router.post("/mode")
def set_mode(req: ModeRequest):
    set_robot_mode(req.mode)
    return {"mode": req.mode}


@router.post("/manual")
def manual(req: ManualCommandRequest):
    if get_robot_mode() != RobotMode.MANUAL:
        raise HTTPException(
            status_code=400,
            detail="Robot is not in MANUAL mode"
        )
    set_manual_command(req.command)
    return {"command": req.command}
