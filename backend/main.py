from core.loop import run_robot
from core.state import RobotState, RobotMode
import threading
import time

if __name__ == "__main__":
    state = RobotState()

    # Demo: switch modes over time
    def demo():
        time.sleep(2)
        state.set_mode(RobotMode.AUTO)
        time.sleep(3)
        state.set_manual_command("LEFT")
        time.sleep(2)
        state.set_mode(RobotMode.TRACK_BALL)
        time.sleep(3)
        state.set_mode(RobotMode.IDLE)

    threading.Thread(target=demo, daemon=True).start()
    run_robot(state)
