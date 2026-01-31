from enum import Enum
from typing import Dict
from core.safety import SafetyState
from core.decision import DecisionIntent

class MotionDirection(Enum):
    FORWARD = "FORWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    BACK = "BACK"
    STOP = "STOP"   

class MotionPlanner:
    """
    TB-10: Motion Strategy / Obstacle Avoidance

    Converts:
    - high-level intent
    - safety state
    - obstacle distances

    Into:
    - a single movement direction

    This module does NOT:
    - control motors
    - read sensors
    - perform safety evaluation
    """

    def decide_direction(
            self,
            intent: DecisionIntent,
            safety_state: SafetyState,
            distances: Dict[str, int]
    ) -> MotionDirection:
        
        # Rule 1: Intent STOP always wins
        if intent == DecisionIntent.STOP:
            return MotionDirection.STOP
        
        front = distances.get("front", 0)
        left = distances.get("left", 0)
        right = distances.get("right", 0)

        # Rule 2: Safety CLEAR -> move forward
        if safety_state == SafetyState.CLEAR:
            return MotionDirection.FORWARD
        
        # Rule 3: Safety WARNING 
        if safety_state == SafetyState.WARNING:
            # Front is gettingn close -> avoid
            if front < left or front < right:
                return(
                    MotionDirection.LEFT
                    if left >= right
                    else MotionDirection.RIGHT
                )
            #Otherwise path is still usabel
            return MotionDirection.FORWARD
        
        # Rule 4: Safety BLOCKED
        if safety_state == SafetyState.BLOCKED:
            if left > front:
                return MotionDirection.LEFT
            if right > front:
                return MotionDirection.RIGHT
            
            #Assume back is free in simulation
            return MotionDirection.BACK
        
        #Fail-safe fallback
        return MotionDirection.STOP