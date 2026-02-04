# backend/core/decision.py

from enum import Enum
from core.safety import SafetyState
from core.state import RobotMode, get_manual_command


class DecisionIntent(Enum):
    STOP = "STOP"
    MANUAL = "MANUAL"
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
    Outputs intent only.
    """

    def decide(
        self,
        safety_state: SafetyState,
        robot_mode: RobotMode,
        ball_seen: bool = False,
        owner_seen: bool = False
    ) -> DecisionIntent:

        # 1️⃣ Safety override (always)
        if safety_state == SafetyState.BLOCKED:
            return DecisionIntent.STOP

        # 2️⃣ MANUAL MODE
        if robot_mode == RobotMode.MANUAL:
            manual_cmd = get_manual_command()
            if manual_cmd:
                return DecisionIntent(manual_cmd)
            return DecisionIntent.STOP

        # 3️⃣ TRACK BALL
        if robot_mode == RobotMode.TRACK_BALL:
            if ball_seen:
                return DecisionIntent.TRACK_BALL
            return DecisionIntent.STOP

        # 4️⃣ Follow owner (not used yet)
        if robot_mode == RobotMode.FOLLOW_OWNER and owner_seen:
            return DecisionIntent.FOLLOW_OWNER

        # 5️⃣ Auto mode
        if robot_mode == RobotMode.AUTO:
            return DecisionIntent.MOVE_FORWARD

        # 6️⃣ Idle fallback
        return DecisionIntent.STOP
