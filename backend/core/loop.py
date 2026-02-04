# backend/core/loop.py

import time

from sensors.obstacle import ObstacleSensor
from core.safety import SafetyEvaluator
from core.decision import DecisionEngine
from core.motion import MotionPlanner
from core.state import get_robot_mode
from core.perception import PerceptionEngine
from control.motor import execute_motion

_last_snapshot = {}

def get_last_snapshot():
    return _last_snapshot


def run_brain_loop():
    global _last_snapshot

    sensor = ObstacleSensor()
    perception = PerceptionEngine()
    safety = SafetyEvaluator()
    decision = DecisionEngine()
    motion = MotionPlanner()

    print("🧠 Robo brain running (BALL TRACKING INTEGRATED)")

    while True:
        # 1️⃣ Distance sensing (AUTO / SAFETY)
        distances = sensor.get_distances()

        # 2️⃣ Vision perception (TRACK_BALL only)
        ball_data = perception.get_perception()

        # 3️⃣ Safety
        safety_state = safety.evaluate(distances)

        # 4️⃣ Decision
        intent = decision.decide(
            safety_state=safety_state,
            robot_mode=get_robot_mode(),
            ball_seen=ball_data["ball_seen"],
            owner_seen=False,
        )

        # 5️⃣ Motion
        direction = motion.decide_direction(
            intent=intent,
            safety_state=safety_state,
            distances=distances,
        )

        # 6️⃣ Execute
        execute_motion(direction)

        # 7️⃣ Snapshot (API / Dashboard)
        _last_snapshot = {
            "mode": get_robot_mode().name,
            "safety": safety_state.name,
            "intent": intent.name,
            "motion": direction.name,
            "distances": distances,
            "ball": ball_data,
        }

        time.sleep(0.2)
