from enum import Enum

class RobotMode(Enum):
    IDLE = 0
    MANUAL = 1
    AUTO = 2
    TRACK_BALL = 3
    FOLLOW_OWNER = 4

class RobotState:
    def __init__(self):
        self.mode = RobotMode.IDLE
