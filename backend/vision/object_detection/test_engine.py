import cv2
import time

from vision.camera import Camera
from vision.object_detection.engine import ObjectDetectionEngine


def main():
    cam = Camera()
    engine = ObjectDetectionEngine()

    print("🧪 Testing ObjectDetectionEngine (labels only)")
    print("Press Q to quit\n")

    while True:
        frame = cam.get_frame()
        if frame is None:
            continue

        labels = engine.detect(frame)

        # ---- CONSOLE OUTPUT ----
        if labels:
            print(f"[{time.strftime('%H:%M:%S')}] Objects:", labels)

        # ---- SIMPLE VISUAL (DEBUG ONLY) ----
        cv2.putText(
            frame,
            f"Detected: {', '.join(labels) if labels else 'None'}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

        cv2.imshow("ObjectDetectionEngine Test", frame)

        if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
