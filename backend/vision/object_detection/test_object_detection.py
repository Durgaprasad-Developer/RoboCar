import cv2
import time

from backend.vision.camera import Camera
from backend.vision.object_detection.yolo8_detector import YOLOv8Detector
from backend.vision.object_detection.gemini_validator import GeminiValidator

YOLO_INTERVAL = 3
MEMORY_TIMEOUT = 1.2


def draw_yolo(frame, detections):
    for d in detections:
        x1, y1, x2, y2 = d["bbox"]
        label = f"{d['label']} ({d['confidence']:.2f})"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )


def main():
    cam = Camera()
    yolo = YOLOv8Detector()
    gemini = GeminiValidator()

    frame_count = 0
    last_detections = []
    last_time = 0

    print("🚀 YOLO + Gemini (Validator Mode) Running")

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        frame_count += 1

        # ---- YOLO (FAST, LOCAL) ----
        if frame_count % YOLO_INTERVAL == 0:
            detections = yolo.detect(frame)
            if detections:
                last_detections = detections
                last_time = time.time()

                # ---- GEMINI (SLOW, CLOUD, VALIDATOR) ----
                if gemini.should_validate(detections):
                    print("🧠 Gemini validating...")
                    gemini.validate_async(frame, detections[0]["label"])

        # ---- DRAW YOLO MEMORY ----
        if last_detections and (time.time() - last_time) < MEMORY_TIMEOUT:
            draw_yolo(frame, last_detections)

        # ---- DRAW GEMINI RESULT ----
        if gemini.result_text:
            cv2.putText(
                frame,
                f"Gemini: {gemini.result_text}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        cv2.imshow("Robot Vision (YOLO + Gemini Validator)", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
