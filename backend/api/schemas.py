from pydantic import BaseModel
from typing import Literal

class ModeRequest(BaseModel):
    mode: Literal[
        "IDLE",
        "MANUAL",
        "AUTO",
        "TRACK_BALL",
        "FOLLOW_OWNER",
        "DETECT_OBJECT",
    ]

class ManualCommandRequest(BaseModel):
    command: Literal[
        "FORWARD",
        "LEFT",
        "RIGHT",
        "BACK",
        "STOP",
    ]
