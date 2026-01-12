from ultralytics import YOLO

class YOLOv8Detector:
    def __init__(self, confidence=0.4):
        self.model = YOLO("yolov8n.pt")
        self.confidence = confidence
        print("🧠 YOLOv8-nano loaded")

    def detect(self, frame):
        results = self.model(frame, conf=self.confidence, verbose=False)
        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append({
                    "label": label,
                    "confidence": conf,
                    "bbox": (x1, y1, x2, y2)
                })

        return detections
