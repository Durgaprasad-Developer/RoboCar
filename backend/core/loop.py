import time
from core.state import RobotMode
from control import motor

def sense_environment():
    """
    Collect all inputs.
    For TB-2 this is simulated.
    """
    perception = {
        "front_distance": 30,
        "ball_seen": False,
        "owner_seen": False
    }
    return perception

def decide(perception, state):
    """
    Decide what to do based on perception + mode
    """
    # Safety first
    if perception["front_distance"] < 15:
        return "AVOID_OBSTACLE"

    if state.mode == RobotMode.TRACK_BALL:
        if perception["ball_seen"]:
            return "FOLLOW_BALL"
        else:
            return "STOP"

    if state.mode == RobotMode.AUTO:
        return "MOVE_FORWARD"

    if state.mode == RobotMode.IDLE:
        return "STOP"

    return "STOP"

def act(decision):
    """
    Convert decision into motor action
    """
    if decision == "MOVE_FORWARD":
        motor.move_forward()
    elif decision == "FOLLOW_BALL":
        motor.move_forward()
    elif decision == "AVOID_OBSTACLE":
        motor.turn_left()
    else:
        motor.stop()
        
def run_robot(state):
    print("🤖 Robot brain started")

    while True:
        perception = sense_environment()
        decision = decide(perception, state)
        act(decision)

        time.sleep(0.5)  # control loop speed

