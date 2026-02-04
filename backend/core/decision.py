# backend/core/decision.py

from enum import Enum
from core.safety import SafetyState
from core.state import RobotMode, get_manual_command


class DecisionIntent(Enum):
    STOP = "STOP"
    TRACK_BALL = "TRACK_BALL"
    FOLLOW_OWNER = "FOLLOW_OWNER"
    MOVE_FORWARD = "MOVE_FORWARD"

    # Manual directions
    FORWARD = "FORWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    BACK = "BACK"


class DecisionEngine:
    """
    High-level decision maker.
    Outputs INTENT only.
    """

    def decide(
        self,
        safety_state: SafetyState,
        robot_mode: RobotMode,
        ball_seen: bool = False,
        owner_seen: bool = False,
    ) -> DecisionIntent:

        # 1️⃣ SAFETY FIRST
        if safety_state == SafetyState.BLOCKED:
            return DecisionIntent.STOP

        # 2️⃣ MANUAL MODE
        if robot_mode == RobotMode.MANUAL:
            cmd = get_manual_command()
            if cmd:
                return DecisionIntent(cmd)
            return DecisionIntent.STOP

        # 3️⃣ TRACK BALL
        if robot_mode == RobotMode.TRACK_BALL:
            return (
                DecisionIntent.TRACK_BALL
                if ball_seen
                else DecisionIntent.STOP
            )

        # 4️⃣ FOLLOW OWNER (DETECTION ONLY)
        if robot_mode == RobotMode.FOLLOW_OWNER:
            return DecisionIntent.FOLLOW_OWNER if owner_seen else DecisionIntent.STOP

        # 5️⃣ AUTO MODE
        if robot_mode == RobotMode.AUTO:
            return DecisionIntent.MOVE_FORWARD

        # 6️⃣ IDLE / FALLBACK
        return DecisionIntent.STOP
