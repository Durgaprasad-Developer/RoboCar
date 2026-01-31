# backend/core/safety.py

from enum import IntEnum
from typing import Dict


class SafetyState(IntEnum):
    CLEAR = 0
    WARNING = 1
    BLOCKED = 2


class SafetyEvaluator:
    """
    Forward-focused safety evaluation.
    Side obstacles are handled by motion strategy.
    """

    def __init__(self, warning_distance: int = 40, danger_distance: int = 10):
        self.warning_distance = warning_distance
        self.danger_distance = danger_distance

    def evaluate(self, distances: Dict[str, int]) -> SafetyState:
        #Fail-safe
        if not distances or "front" not in distances:
            return SafetyState.BLOCKED
        
        front = distances["front"]

        # Front completely blocked
        if front <= self.danger_distance:
            return SafetyState.BLOCKED
        
        #Front gettingn close -> prepare avoidance
        if front <= self.warning_distance:
            return SafetyState.WARNING
        
        #Default: forward is safe
        return SafetyState.CLEAR