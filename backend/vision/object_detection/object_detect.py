import cv2
import numpy as np
import os

class ObjectDetector:
    def __init__(self, confidence_threshold=0.5, nms_threshold=0.4):
        base_path = os.path.dirname(__file__)
        model_path = os.path.join(base_path, "models")

        weights = os.path.join(model_path, "yolov3-tiny.weights")
        config = os.path.join(model_path, "yolov3-tiny.cfg")
        names = os.path.join(model_path, "coco.names")

        self.net = cv2.dnn.readNet(weights, config)

        with open(names, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]

        self.confidence_threshold = confidence_threshold
        self.nms_threshold = nms_threshold

        print("🧠 Object Detector initialized")

    def detect(self, frame):
        height, width, _ = frame.shape

        blob = cv2.dnn.blobFromImage(
            frame, 1 / 255.0, (416, 416), swapRB=True, crop=False
        )

        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)

        boxes = []
        confidences = []
        class_ids = []

        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > self.confidence_threshold:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indices = cv2.dnn.NMSBoxes(
            boxes, confidences, self.confidence_threshold, self.nms_threshold
        )

        detections = []

        for i in indices:
            i = i[0] if isinstance(i, (list, tuple, np.ndarray)) else i
            x, y, w, h = boxes[i]
            detections.append({
                "label": self.classes[class_ids[i]],
                "confidence": confidences[i],
                "bbox": (x, y, w, h)
            })

        return detections
