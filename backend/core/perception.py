# backend/core/perception.py

from vision.ball_tracking.ball_track import BallTracker
from vision.face_recognition.engine import FaceRecognitionEngine
from core.state import get_robot_mode, RobotMode


class PerceptionEngine:
    """
    TB-14 FINAL PERCEPTION

    - Uses ONE shared camera frame
    - Mode-gated vision execution
    - Returns FACTS only (no decisions)
    """

    def __init__(self):
        self.ball_tracker = BallTracker()
        self.face_engine = FaceRecognitionEngine()

    # ------------------------
    # INTERNAL RESET HELPERS
    # ------------------------
    def _reset_ball_tracker(self):
        self.ball_tracker.state.center = None
        self.ball_tracker.state.radius = None
        self.ball_tracker.state.missed = 0
        self.ball_tracker.state.trail.clear()

    # ------------------------
    # MAIN PERCEPTION API
    # ------------------------
    def get_perception(self, frame):
        """
        Returns a dict with perception facts.
        """

        perception = {
            # Ball tracking
            "ball_seen": False,
            "ball_position": "NONE",

            # Face recognition
            "owner_status": "NONE",  # OWNER | UNKNOWN | NONE
            # "objectDetected": "NONE"
        }

        mode = get_robot_mode()

        if frame is None:
            self._reset_ball_tracker()
            return perception

        # ========================
        # BALL TRACKING
        # ========================
        if mode == RobotMode.TRACK_BALL:
            _, center = self.ball_tracker.run(frame)
            state = self.ball_tracker.state

            if (
                center is not None
                and state.radius is not None
                and state.radius >= 8
                and state.missed <= 1
            ):
                perception["ball_seen"] = True

                x = center[0]
                w = frame.shape[1]

                if x < w * 0.4:
                    perception["ball_position"] = "LEFT"
                elif x > w * 0.6:
                    perception["ball_position"] = "RIGHT"
                else:
                    perception["ball_position"] = "CENTER"

        else:
            # Ensure no ghost ball data
            self._reset_ball_tracker()

        # ========================
        # FACE RECOGNITION
        # ========================
        if mode == RobotMode.FOLLOW_OWNER:
            perception["owner_status"] = self.face_engine.detect(frame)

        return perception
