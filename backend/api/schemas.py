from pydantic import BaseModel
from typing import Literal


class ModeRequest(BaseModel):
    mode: Literal["IDLE", "AUTO", "MANUAL", "TRACK_BALL"]


class ManualCommandRequest(BaseModel):
    command: Literal["FORWARD", "LEFT", "RIGHT", "BACK", "STOP"]
    