import time
from core.state import RobotMode
from control import motor

def sense_environment():
    # TB-3 still simulated
    return {
        "front_distance": 30,   # cm
        "ball_seen": False,
        "owner_seen": False
    }

def decide(perception, state):
    # --- Safety override (always) ---
    if perception["front_distance"] < 15:
        return "AVOID_OBSTACLE"

    # --- Manual has highest priority ---
    if state.mode == RobotMode.MANUAL and state.manual_command:
        return state.manual_command

    # --- Mode-gated behaviors ---
    if state.mode == RobotMode.TRACK_BALL:
        return "FOLLOW_BALL" if perception["ball_seen"] else "STOP"

    if state.mode == RobotMode.FOLLOW_OWNER:
        return "FOLLOW_OWNER" if perception["owner_seen"] else "STOP"

    if state.mode == RobotMode.AUTO:
        return "MOVE_FORWARD"

    if state.mode == RobotMode.IDLE:
        return "STOP"

    return "STOP"

def act(decision):
    if decision == "MOVE_FORWARD":
        motor.move_forward()
    elif decision == "FOLLOW_BALL":
        motor.move_forward()
    elif decision == "FOLLOW_OWNER":
        motor.move_forward()
    elif decision == "LEFT":
        motor.turn_left()
    elif decision == "RIGHT":
        motor.turn_right()
    elif decision == "BACK":
        motor.move_backward()
    elif decision == "AVOID_OBSTACLE":
        motor.turn_left()  # full logic comes in TB-8
    else:
        motor.stop()

def run_robot(state):
    print("🤖 Robot brain running (TB-3)")
    while True:
        perception = sense_environment()
        decision = decide(perception, state)
        act(decision)
        time.sleep(0.5)
