import cv2
import time

from backend.vision.camera import Camera
from backend.vision.object_detection import YOLOv8Detector, GeminiVisionDetector

YOLO_INTERVAL = 3                 # run YOLO every N frames
YOLO_FAIL_THRESHOLD = 10          # consecutive fails before Gemini
GEMINI_COOLDOWN = 30              # seconds
MEMORY_TIMEOUT = 1.0              # seconds to keep last detection


def draw(frame, detections, source):
    for d in detections:
        x1, y1, x2, y2 = d["bbox"]
        label = f"{d['label']} ({source})"
        color = (0, 255, 0) if source == "YOLOv8" else (0, 0, 255)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            frame, label, (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2
        )


def main():
    cam = Camera()
    yolo = YOLOv8Detector()
    gemini = GeminiVisionDetector()

    frame_count = 0
    yolo_fail_count = 0
    last_gemini_time = 0

    last_detections = []
    last_source = None
    last_detection_time = 0

    print("🚀 Optimized Object Detection Running")

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        frame_count += 1
        detections = []

        # -------- YOLO (fast, periodic) --------
        if frame_count % YOLO_INTERVAL == 0:
            detections = yolo.detect(frame)
            if detections:
                yolo_fail_count = 0
                last_detections = detections
                last_source = "YOLOv8"
                last_detection_time = time.time()
            else:
                yolo_fail_count += 1

        # -------- GEMINI (slow, rare) --------
        now = time.time()
        if (
            yolo_fail_count >= YOLO_FAIL_THRESHOLD
            and (now - last_gemini_time) > GEMINI_COOLDOWN
        ):
            print("🔴 Triggering Gemini fallback")
            detections = gemini.detect(frame)
            last_gemini_time = now

            if detections:
                last_detections = detections
                last_source = "GEMINI"
                last_detection_time = now
                yolo_fail_count = 0

        # -------- MEMORY (anti-blink) --------
        if last_detections and (time.time() - last_detection_time) < MEMORY_TIMEOUT:
            draw(frame, last_detections, last_source)

        cv2.imshow("Robot Vision (Optimized)", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
