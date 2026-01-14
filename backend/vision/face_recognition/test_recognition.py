import cv2
from insightface.app import FaceAnalysis
from vision.camera import Camera
from .recognizer import OwnerRecognizer
from .visualize import draw_face_ui

def main():
    app = FaceAnalysis(name="buffalo_l")
    app.prepare(ctx_id=0, det_size=(640, 640))

    camera = Camera()
    recognizer = OwnerRecognizer()

    print("🧪 Testing face recognition only (NO tracking)")

    while True:
        frame = camera.get_frame()
        if frame is None:
            continue

        faces = app.get(frame)

        if faces:
            f = faces[0]
            label, score = recognizer.recognize(f.embedding)
            draw_face_ui(frame, f, label, score)

        cv2.imshow("Face Recognition Test", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
