from vision.object_detection.yolo8_detector import YOLOv8Detector

class ObjectDetectionEngine:
    """
    Brain-safe object detection engine

    - No camera ownership
    - No UI drawing
    - No tracking
    - Returns labels only
    """

    def __init__(self):
        self.detector = YOLOv8Detector()
        print("🧠 ObjectDetectionEngine initialized")

    def detect(self, frame):
        if frame is None:
            return []

        detections = self.detector.detect(frame)

        # Only unique labels (dashboard friendly)
        labels = list({d["label"] for d in detections})
        return labels
