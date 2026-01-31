from sensors.obstacle import ObstacleSensor
from core.safety import SafetyEvaluator, SafetyState
from core.decision import DecisionEngine, DecisionIntent
from core.motion import MotionPlanner, MotionDirection
from core.state import RobotMode
import time

#Initialize modulees
sensor = ObstacleSensor()
safety = SafetyEvaluator()
decision_engine = DecisionEngine()
motion_planner = MotionPlanner()

# Robot configuration
robot_mode = RobotMode.AUTO
ball_seen = False
owner_seen = False

print("Robot Mode: ", robot_mode)
print("-" * 50)

# Run simulation loop
for cycle in range(20):
    distances = sensor.get_distances()
    safety_state = safety.evaluate(distances)

    intent = decision_engine.decide(
        safety_state=safety_state,
        robot_mode=robot_mode,
        ball_seen=ball_seen,
        owner_seen=owner_seen,
    )

    direction = motion_planner.decide_direction(
        intent=intent,
        safety_state=safety_state,
        distances=distances,
    )

    print(f"Cycle {cycle + 1}")
    print("Distances:", distances)
    print("Safety:", safety_state.name, f"({int(safety_state)})")
    print("Intent:", intent.name)
    print("Direction:", direction.name)
    print("-" * 50)

    time.sleep(0.5)