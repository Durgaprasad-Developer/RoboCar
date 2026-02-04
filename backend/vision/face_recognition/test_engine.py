import cv2
from vision.camera import Camera
from vision.face_recognition.engine import FaceRecognitionEngine

def main():
    cam = Camera()
    engine = FaceRecognitionEngine()

    print("🧪 Testing FaceRecognitionEngine (ESC to quit)")

    while True:
        frame = cam.get_frame()
        if frame is None:
            continue

        status = engine.detect(frame)
        print("OWNER STATUS:", status)

        cv2.imshow("Engine Test", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
