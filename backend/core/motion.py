from enum import Enum
from typing import Dict, Optional
from core.safety import SafetyState
from core.decision import DecisionIntent


class MotionDirection(Enum):
    FORWARD = "FORWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    BACK = "BACK"
    STOP = "STOP"


class MotionPlanner:
    """
    TB-14 FINAL (CORRECT)
    - AUTO never leaks into TRACK
    - Ball position drives motion
    """

    def decide_direction(
        self,
        intent: DecisionIntent,
        safety_state: SafetyState,
        distances: Dict[str, int],
        ball_position: Optional[str] = None,
    ) -> MotionDirection:

        # 1️⃣ STOP ALWAYS WINS
        if intent == DecisionIntent.STOP:
            return MotionDirection.STOP

        # 2️⃣ MANUAL OVERRIDE
        if intent in (
            DecisionIntent.FORWARD,
            DecisionIntent.LEFT,
            DecisionIntent.RIGHT,
            DecisionIntent.BACK,
        ):
            if safety_state == SafetyState.BLOCKED:
                return MotionDirection.STOP
            return MotionDirection(intent.value)

        # 3️⃣ TRACK BALL (🔥 HARD MODE GATE)
        if intent == DecisionIntent.TRACK_BALL:
            if safety_state == SafetyState.BLOCKED:
                return MotionDirection.STOP

            if ball_position == "LEFT":
                return MotionDirection.LEFT

            if ball_position == "RIGHT":
                return MotionDirection.RIGHT

            if ball_position == "CENTER":
                return MotionDirection.FORWARD

            return MotionDirection.STOP   # ball lost

        # 4️⃣ AUTO MODE (ONLY WHEN INTENT == MOVE_FORWARD)
        if intent == DecisionIntent.MOVE_FORWARD:
            front = distances.get("front", 0)
            left = distances.get("left", 0)
            right = distances.get("right", 0)

            if safety_state == SafetyState.CLEAR:
                return MotionDirection.FORWARD

            if safety_state == SafetyState.WARNING:
                if front < left or front < right:
                    return MotionDirection.LEFT if left >= right else MotionDirection.RIGHT
                return MotionDirection.FORWARD

            if safety_state == SafetyState.BLOCKED:
                if left > front:
                    return MotionDirection.LEFT
                if right > front:
                    return MotionDirection.RIGHT
                return MotionDirection.BACK

        # 5️⃣ FINAL FAILSAFE
        return MotionDirection.STOP
