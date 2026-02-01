# backend/api/routes.py

from fastapi import APIRouter, HTTPException

from api.schemas import ModeRequest, ManualCommandRequest

from core.state import (
    get_robot_mode,
    set_robot_mode,
    get_manual_command,
    set_manual_command,
)

from core.loop import get_last_snapshot

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/status")
def get_status():
    """
    Read-only view of robot brain state.
    """
    snapshot = get_last_snapshot()

    return {
        "mode": snapshot["mode"],
        "safety": snapshot["safety"],
        "intent": snapshot["intent"],
        "motion": snapshot["motion"],
        "distances": snapshot["distances"],
    }

@router.post("/mode")
def st_mode(req:ModeRequest):
    set_robot_mode(req.mode)
    return {"mode": req.mode}

@router.post("/manual")
def manual_command(req: ManualCommandRequest):
    if get_robot_mode() != "MANUAL":
        raise HTTPException(
            status_code=400,
            detail="Robot is not in MANUAL mode",
            )
    
    set_manual_command(req.command)
    return {"command": req.command}