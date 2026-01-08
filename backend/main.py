from core.loop import run_robot
from core.state import RobotState, RobotMode

if __name__ == "__main__":
    state = RobotState()

    # TEMP: set initial mode
    state.mode = RobotMode.AUTO

    run_robot(state)
