# backend/sensors/obstacle.py

import random
from typing import Dict


class ObstacleSensor:
    """
    Simulated obstacle sensor.
    Provides raw distance data only (in cm).
    """

    def __init__(self, min_distance: int = 5, max_distance: int = 200):
        self.min_distance = min_distance
        self.max_distance = max_distance

    def get_distances(self) -> Dict[str, int]:
        return {
            "front": random.randint(self.min_distance, self.max_distance),
            "left": random.randint(self.min_distance, self.max_distance),
            "right": random.randint(self.min_distance, self.max_distance),
        }
