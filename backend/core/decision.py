from enum import Enum
from core.safety import SafetyState
from core.state import RobotMode

class DecisionIntent(Enum):
    STOP = "STOP"
    MANUAL = "MANUAL"
    TRACK_BALL = "TRACK_BALL"
    FOLLOW_OWNER = "FOLLOW_OWNER"
    MOVE_FORWARD = "MOVE_FORWARD"

class DecisionEngine:
    """
    High-level decision maker.
    Outputs intent only
    """

    def decide(
            self, 
            safety_state: SafetyState,
            robot_mode: RobotMode,
            ball_seen: bool = False,
            owner_seen: bool = False
    ) -> DecisionIntent:
        #1. Safety override

        if safety_state == SafetyState.BLOCKED:
            return DecisionIntent.STOP
        
        #2. Manual mode
        if robot_mode == RobotMode.MANUAL:
            return DecisionIntent.MANUAL
        
        #3 Track ball
        if robot_mode == RobotMode.TRACK_BALL and ball_seen:
            return DecisionIntent.TRACK_BALL
        
        #4 Follow owner
        if robot_mode == RobotMode.FOLLOW_OWNER and owner_seen:
            return DecisionIntent.FOLLOW_OWNER
        
        #5 Auto mode
        if robot_mode == robot_mode.AUTO:
            return DecisionIntent.MOVE_FORWARD
        
        #6. Idle fallback
        return DecisionIntent.STOP