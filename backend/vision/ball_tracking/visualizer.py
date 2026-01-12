import cv2

def draw(frame, center, radius, trail):
    h, w, _ = frame.shape
    cx, cy = center

    # Ball
    cv2.circle(frame, center, radius, (0, 255, 0), 2)
    cv2.circle(frame, center, 4, (0, 0, 255), -1)

    # Axis
    cv2.line(frame, (cx, 0), (cx, h), (0, 255, 255), 1)
    cv2.line(frame, (0, cy), (w, cy), (0, 255, 255), 1)

    # Coordinates
    cv2.putText(
        frame,
        f"({cx}, {cy})",
        (cx + 10, cy - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # 🔥 Draw full trail
    for i in range(1, len(trail)):
        cv2.line(frame, trail[i - 1], trail[i], (255, 0, 0), 2)
