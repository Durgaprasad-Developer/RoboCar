from vision.ball_tracking.ball_track import BallTracker
from vision.face_recognition.engine import FaceRecognitionEngine
from vision.object_detection.engine import ObjectDetectionEngine
from core.state import get_robot_mode, RobotMode


class PerceptionEngine:
    """
    TB-14 FINAL PERCEPTION

    - One shared camera frame
    - Mode gated
    - Facts only
    """

    def __init__(self):
        self.ball_tracker = BallTracker()
        self.face_engine = FaceRecognitionEngine()
        self.object_engine = ObjectDetectionEngine()

    def _reset_ball(self):
        self.ball_tracker.state.center = None
        self.ball_tracker.state.radius = None
        self.ball_tracker.state.missed = 0
        self.ball_tracker.state.trail.clear()

    def get_perception(self, frame):
        perception = {
            "ball_seen": False,
            "ball_position": "NONE",
            "owner_status": "NONE",
            "objects": [],              # 🔥 NEW
        }

        mode = get_robot_mode()

        if frame is None:
            self._reset_ball()
            return perception

        # 🎾 BALL TRACKING
        if mode == RobotMode.TRACK_BALL:
            _, center = self.ball_tracker.run(frame)
            state = self.ball_tracker.state

            if (
                center
                and state.radius
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
            self._reset_ball()

        # 👤 FACE RECOGNITION
        if mode == RobotMode.FOLLOW_OWNER:
            perception["owner_status"] = self.face_engine.detect(frame)

        # 📦 OBJECT DETECTION
        if mode == RobotMode.DETECT_OBJECT:
            perception["objects"] = self.object_engine.detect(frame)

        return perception
