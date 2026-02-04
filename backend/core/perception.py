from vision.ball_tracking.ball_track import BallTracker
from core.state import get_robot_mode, RobotMode


class PerceptionEngine:
    """
    TB-14 (Ball Tracking – FIXED)
    - Strong validation
    - No ghost detections
    """

    def __init__(self):
        self.ball_tracker = BallTracker()

    def reset(self):
        # HARD RESET tracker state
        self.ball_tracker.state.center = None
        self.ball_tracker.state.radius = None
        self.ball_tracker.state.missed = 0
        self.ball_tracker.state.trail.clear()

    def get_perception(self, frame):
        perception = {
            "ball_seen": False,
            "ball_position": "NONE",
        }

        # 🔒 Only TRACK_BALL uses vision
        if get_robot_mode() != RobotMode.TRACK_BALL:
            self.reset()
            return perception

        if frame is None:
            self.reset()
            return perception

        frame_out, center = self.ball_tracker.run(frame)

        # 🔥 HARD VALIDATION
        state = self.ball_tracker.state

        # 1️⃣ Center must exist
        if center is None:
            return perception

        # 2️⃣ Radius must be sane
        if state.radius is None or state.radius < 8:
            return perception

        # 3️⃣ Must be recently seen (no stale ghost)
        if state.missed > 1:
            return perception

        # ✅ Now we trust it
        perception["ball_seen"] = True

        x = center[0]
        w = frame.shape[1]

        if x < w * 0.4:
            perception["ball_position"] = "LEFT"
        elif x > w * 0.6:
            perception["ball_position"] = "RIGHT"
        else:
            perception["ball_position"] = "CENTER"

        return perception
