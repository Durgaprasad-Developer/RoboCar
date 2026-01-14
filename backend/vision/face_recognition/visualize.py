# vision/face_recognition/visualize.py

import cv2

GREEN = (0, 255, 0)
RED = (0, 0, 255)

def draw_face_ui(frame, face, label, score):
    x1, y1, x2, y2 = map(int, face.bbox)
    color = GREEN if label == "OWNER" else RED

    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    cv2.putText(
        frame,
        f"{label} {score:.2f}",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        color,
        2
    )
