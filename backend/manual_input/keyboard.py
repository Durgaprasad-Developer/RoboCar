# backend/manual_input/keyboard.py

"""
TB-13 Keyboard Manual Input

Converts keyboard presses into HIGH-LEVEL manual commands.
Writes ONLY to core/state.py.
"""

from pynput import keyboard
from core.state import (
    get_robot_mode,
    set_manual_command,
    clear_manual_command,
    RobotMode,
)

KEY_MAP = {
    "w": "FORWARD",
    "a": "LEFT",
    "s": "BACK",
    "d": "RIGHT",
    " ": "STOP",
}


def on_press(key):
    try:
        char = key.char
    except AttributeError:
        return

    if get_robot_mode().name != RobotMode.MANUAL:
        return

    if char in KEY_MAP:
        cmd = KEY_MAP[char]
        set_manual_command(cmd)
        print(f"⌨️ MANUAL INPUT: {cmd}")


def on_release(key):
    if get_robot_mode().name != RobotMode.MANUAL:
        return

    try:
        if key.char in ["w", "a", "s", "d"]:
            clear_manual_command()
    except AttributeError:
        pass


def start_keyboard():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.daemon = True
    listener.start()
    print("⌨️ Keyboard manual control ready")
