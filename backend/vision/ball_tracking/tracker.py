from collections import deque
from .config import MAX_MISSED_FRAMES

class TrackerState:
    def __init__(self, trail_length=30):
        self.center = None
        self.radius = None
        self.missed = 0

        # 🔥 store trail history
        self.trail = deque(maxlen=trail_length)

    def update(self, detected):
        if detected is None:
            self.missed += 1
            if self.missed > MAX_MISSED_FRAMES:
                self.center = None
                self.radius = None
                self.trail.clear()
            return self.center, self.radius, list(self.trail)

        cx, cy, radius = detected
        self.center = (cx, cy)
        self.radius = radius
        self.missed = 0

        # add to trail
        self.trail.append(self.center)

        return self.center, self.radius, list(self.trail)