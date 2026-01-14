from .config import LOWER_HSV, UPPER_HSV, MIN_RADIUS
from .preprocess import preprocess
from .detector import find_contours
from .selector import select_ball
from .tracker import TrackerState
from .visualizer import draw

class BallTracker:
    def __init__(self):
        self.state = TrackerState()

    def run(self, frame):
        mask = preprocess(frame, LOWER_HSV, UPPER_HSV)
        contours = find_contours(mask)
        detected = select_ball(contours, MIN_RADIUS)

        center, radius, trail = self.state.update(detected)

        if center and radius:
            draw(frame, center, radius, trail)

        return frame, center