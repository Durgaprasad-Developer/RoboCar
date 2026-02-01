#backend/core/loop.py

import time

from sensors.obstacle import ObstacleSensor
from core.safety import SafetyEvaluator
from core.decision import DecisionEngine
from core.motion import MotionPlanner
from core.state import (
    get_robot_mode,
    get_manual_command,
)
from control.motor import execute_motion

_last_snapshot = {}

def get_last_snapshot():
    return _last_snapshot

def run_brain_loop():
    global _last_snapshot

    sensor = ObstacleSensor()
    safety = SafetyEvaluator()
    decision = DecisionEngine()
    motion = MotionPlanner()

    print("Root brain running (TB-11)")

    while True:
        # 1. Sense
        distances = sensor.get_distances()

        # 2, Safety
        safety_state = safety.evaluate(distances)

        # 3. Decide
        robot_mode = get_robot_mode()
        manual_cmd = get_manual_command()

        intent = decision.decide(
            safety_state=safety_state,
            robot_mode=robot_mode,
            ball_seen=False,
            owner_seen=False,
        )

        # 4. Motion strategy
        direction = motion.decide_direction(
            intent=intent,
            safety_state=safety_state,
            distances=distances,
        )

        # 5. Execute (still mocked)
        execute_motion(direction)

        # 6. Snapshot for API
        _last_snapshot = {
            "mode": robot_mode.name,
            "safety": safety_state.name,
            "intent": intent.name,
            "motion": direction.name,
            "distances": distances,
        }

        time.sleep(0.2)


