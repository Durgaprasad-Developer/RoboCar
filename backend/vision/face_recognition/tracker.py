# vision/face_recognition/tracker.py
import cv2

class FaceTracker:
    def __init__(self):
        self.tracker = None
        self.active = False

    def start(self, frame, bbox):
        self.tracker = cv2.TrackerMOSSE_create()
        self.tracker.init(frame, bbox)
        self.active = True

    def update(self, frame):
        if not self.active:
            return None

        ok, box = self.tracker.update(frame)
        if not ok:
            self.active = False
            return None

        x, y, w, h = map(int, box)
        return (x, y, x + w, y + h)
