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
        self.manual_command = None  # 'FORWARD', 'LEFT', etc.

    # ---- Mode setters (dashboard will call these) ----
    def set_mode(self, mode: RobotMode):
        self.mode = mode
        self.manual_command = None  # clear manual command on mode switch

    def set_manual_command(self, cmd: str):
        self.mode = RobotMode.MANUAL
        self.manual_command = cmd

    def clear_manual(self):
        self.manual_command = None
