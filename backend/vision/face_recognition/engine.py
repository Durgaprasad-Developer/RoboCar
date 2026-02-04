from insightface.app import FaceAnalysis
from vision.face_recognition.recognizer import OwnerRecognizer


class FaceRecognitionEngine:
    """
    Brain-safe face recognition engine

    - No camera ownership
    - No UI drawing
    - Returns ONLY:
        "OWNER" | "UNKNOWN" | "NONE"
    """

    def __init__(self):
        try:
            self.app = FaceAnalysis(name="buffalo_l")
            self.app.prepare(ctx_id=0, det_size=(640, 640))
            self.recognizer = OwnerRecognizer()
            self.enabled = True
            print("🧠 FaceRecognitionEngine READY")
        except Exception as e:
            print("⚠️ Face recognition disabled:", e)
            self.enabled = False

    def detect(self, frame) -> str:
        """
        Returns:
        - "OWNER"
        - "UNKNOWN"
        - "NONE"
        """

        if not self.enabled or frame is None:
            return "NONE"

        faces = self.app.get(frame)

        if not faces:
            return "NONE"

        # Take the most confident face
        face = max(faces, key=lambda f: f.det_score)

        label, score = self.recognizer.recognize(face.embedding)

        return label  # "OWNER" or "UNKNOWN"
