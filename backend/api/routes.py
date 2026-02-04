from fastapi import APIRouter, HTTPException
from api.schemas import ModeRequest, ManualCommandRequest
from core.state import (
    get_robot_mode,
    set_robot_mode,
    set_manual_command,
    RobotMode,
)
from core.loop import get_last_snapshot

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/status")
def get_status():
    snapshot = get_last_snapshot()
    return {
        "mode": snapshot["mode"],
        "safety": snapshot["safety"],
        "intent": snapshot["intent"],
        "motion": snapshot["motion"],
        "distances": snapshot["distances"],
        "manual_command": snapshot.get("manual_command"),

        # ✅ ADDED (READ-ONLY, NO LOGIC)
        "perception": snapshot.get("perception"),
    }


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
