# vision/face_recognition/main.py

import cv2
from insightface.app import FaceAnalysis
from vision.camera import Camera
from .recognizer import OwnerRecognizer
from .visualize import draw_face_ui

def main():
    app = FaceAnalysis(name="buffalo_l")
    app.prepare(ctx_id=0, det_size=(640, 640))

    cam = Camera()
    recognizer = OwnerRecognizer()

    print("Face recognition running. Press ESC to exit.")

    while True:
        frame = cam.get_frame()
        if frame is None:
            continue

        faces = app.get(frame)
        if faces:
            face = faces[0]
            label, score = recognizer.recognize(face.embedding)
            draw_face_ui(frame, face, label, score)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
