# backend/core/loop.py

import time

from sensors.obstacle import ObstacleSensor
from core.safety import SafetyEvaluator
from core.decision import DecisionEngine
from core.motion import MotionPlanner
from core.state import get_robot_mode
from core.perception import PerceptionEngine
from control.motor import execute_motion
from vision.camera import Camera

_last_snapshot = {}


def get_last_snapshot():
    return _last_snapshot


def run_brain_loop(camera: Camera):
    global _last_snapshot

    sensor = ObstacleSensor()
    perception = PerceptionEngine()
    safety = SafetyEvaluator()
    decision = DecisionEngine()
    motion = MotionPlanner()

    print("🧠 Robo brain running (BALL TRACKING READY)")

    while True:
        distances = sensor.get_distances()
        frame = camera.get_frame()

        ball_data = perception.get_perception(frame)
        safety_state = safety.evaluate(distances)

        intent = decision.decide(
            safety_state=safety_state,
            robot_mode=get_robot_mode(),
            ball_seen=ball_data["ball_seen"],
            owner_seen=False,
        )

        direction = motion.decide_direction(
            intent=intent,
            safety_state=safety_state,
            distances=distances,
            ball_position=ball_data["ball_position"],
        )


        execute_motion(direction)

        _last_snapshot = {
            "mode": get_robot_mode().name,
            "safety": safety_state.name,
            "intent": intent.name,
            "motion": direction.name,
            "distances": distances,
            "perception": {
                "ball_seen": ball_data["ball_seen"],
                "ball_position": ball_data["ball_position"],
            }
        }

        time.sleep(0.2)
