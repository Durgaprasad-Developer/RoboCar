# backend/control/motor.py

"""
Motor control module (MOCKED).

This file represents the LOWEST layer of the system.
Right now it only prints actions.
Later, this is where GPIO / serial / hardware code will go.

IMPORTANT:
- Do NOT put decision logic here
- Do NOT bypass safety
- Only execute given motion commands
"""

from core.motion import MotionDirection

#Low-level motor primitives (mocked)

def move_foward():
    print("🟢 MOTOR: Moving forward")

def move_backward():
    print("🟡 MOTOR: Moving backward")

def turn_left():
    print("🔵 MOTOR: Turning left")

def turn_right():
    print("🟣 MOTOR: Turning right")

def stop():
    print("🔴 MOTOR: Stopping")

# TB-11 Adapter: MotionDirection -> motor actions

def execute_motion(direction: MotionDirection):
    """
    Adapter between MotionPlanner (TB-10) and motor primitives.

    Input:
    - MotionDirection enum

    Output:
    - Executes motor action (mocked)
    """

    if direction == MotionDirection.FORWARD:
        move_foward()

    elif direction == MotionDirection.LEFT:
        turn_left()

    elif direction == MotionDirection.RIGHT:
        turn_right()

    elif direction == MotionDirection.BACK:
        move_backward()

    else:
        stop()