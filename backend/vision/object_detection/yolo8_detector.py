from ultralytics import YOLO

class YOLOv8Detector:
    def __init__(self, conf=0.4):
        self.model = YOLO("yolov8n.pt")
        self.conf = conf
        print("🧠 YOLOv8-nano loaded")

    def detect(self, frame):
        results = self.model(frame, conf=self.conf, verbose=False)
        detections = []

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append({
                    "label": self.model.names[cls],
                    "confidence": float(box.conf[0]),
                    "bbox": (x1, y1, x2, y2)
                })
        return detections
