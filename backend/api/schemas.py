# backend/ap/schemas.py

from pydantic import BaseModel
from typing import Literal

class ModeRequest(BaseModel):
    mode: Literal["IDLE", "AUTO", "MANUAL", "TRACK"]

class ManualCommandRequest(BaseModel):
    command:Literal["FORWARD", "LEFT", "RIGHT", "BACK", "STOP"]