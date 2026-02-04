from enum import Enum
from typing import Dict
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
    TB-10 + TB-13 + TB-14 (TRACK STOP FIX)
    Converts intent + safety + distances into motion
    """

    def decide_direction(
        self,
        intent: DecisionIntent,
        safety_state: SafetyState,
        distances: Dict[str, int]
    ) -> MotionDirection:

        # 1️⃣ STOP intent always wins
        if intent == DecisionIntent.STOP:
            return MotionDirection.STOP

        # 2️⃣ MANUAL DIRECTION OVERRIDE
        if intent in (
            DecisionIntent.FORWARD,
            DecisionIntent.LEFT,
            DecisionIntent.RIGHT,
            DecisionIntent.BACK,
        ):
            if safety_state == SafetyState.BLOCKED:
                return MotionDirection.STOP
            return MotionDirection(intent.value)

        # 🔥 3️⃣ TRACK BALL LOGIC (ADDED)
        if intent == DecisionIntent.TRACK_BALL:
            # Safety always overrides
            if safety_state == SafetyState.BLOCKED:
                return MotionDirection.STOP

            # Ball lost → STOP (no blind forward)
            return MotionDirection.STOP

        front = distances.get("front", 0)
        left = distances.get("left", 0)
        right = distances.get("right", 0)

        # 4️⃣ AUTO behavior
        if safety_state == SafetyState.CLEAR:
            return MotionDirection.FORWARD

        if safety_state == SafetyState.WARNING:
            if front < left or front < right:
                return (
                    MotionDirection.LEFT
                    if left >= right
                    else MotionDirection.RIGHT
                )
            return MotionDirection.FORWARD

        if safety_state == SafetyState.BLOCKED:
            if left > front:
                return MotionDirection.LEFT
            if right > front:
                return MotionDirection.RIGHT
            return MotionDirection.BACK

        return MotionDirection.STOP
