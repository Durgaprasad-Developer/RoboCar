# backend/core/perception.py

from core.state import RobotMode, get_robot_mode
from vision.camera import Camera
from vision.ball_tracking.ball_track import BallTracker


class PerceptionEngine:
    """
    Ball tracking perception ONLY.
    Camera is LAZY and MODE-GATED.
    """

    def __init__(self):
        self.camera = None
        self.ball_tracker = None

    def _ensure_camera(self):
        if self.camera is None:
            self.camera = Camera()
            self.ball_tracker = BallTracker()

    def _release_camera(self):
        if self.camera:
            self.camera.release()
            self.camera = None
            self.ball_tracker = None

    def get_perception(self):
        # Default safe output
        perception = {
            "ball_seen": False,
            "ball_position": "NONE",
        }

        # 🚨 Only TRACK_BALL is allowed to use camera
        if get_robot_mode() != RobotMode.TRACK_BALL:
            self._release_camera()
            return perception

        # Camera ON only here
        self._ensure_camera()

        frame = self.camera.get_frame()
        if frame is None:
            return perception

        _, center = self.ball_tracker.run(frame)

        if center:
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
