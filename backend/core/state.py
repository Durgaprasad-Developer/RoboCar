# backend/coreee/state.py

from enum import Enum


class RobotMode(Enum):
    IDLE = 0
    MANUAL = 1
    AUTO = 2
    TRACK_BALL = 3
    FOLLOW_OWNER = 4
    DETECT_OBJECT = 5


_current_mode = RobotMode.AUTO
_manual_command = None


def get_robot_mode():
    return _current_mode


def set_robot_mode(mode: str):
    global _current_mode
    _current_mode = RobotMode[mode]
    clear_manual_command()


def get_manual_command():
    return _manual_command


def set_manual_command(cmd: str):
    global _manual_command, _current_mode
    _current_mode = RobotMode.MANUAL
    _manual_command = cmd


def clear_manual_command():
    global _manual_command
    _manual_command = None
