# backend/core/safety.py

from enum import IntEnum
from typing import Dict


class SafetyState(IntEnum):
    CLEAR = 0
    WARNING = 1
    BLOCKED = 2


class SafetyEvaluator:
    def __init__(self, warning_distance: int = 40, danger_distance: int = 10):
        self.warning_distance = warning_distance
        self.danger_distance = danger_distance

    def evaluate(self, distances: Dict[str, int]) -> SafetyState:
        if not distances or "front" not in distances:
            return SafetyState.BLOCKED

        front = distances["front"]

        if front <= self.danger_distance:
            return SafetyState.BLOCKED

        if front <= self.warning_distance:
            return SafetyState.WARNING

        return SafetyState.CLEAR
