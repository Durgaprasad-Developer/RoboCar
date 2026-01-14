import cv2

# =========================
# COLORS (BGR)
# =========================
GREEN = (0, 255, 0)
RED   = (0, 0, 255)


def draw_face_ui(frame, face, label, score):
    """
    CLEAN FaceID-style UI
    No mesh, no grid, no gimmicks.
    Perfect for reels.
    """

    x1, y1, x2, y2 = map(int, face.bbox)
    color = GREEN if label == "OWNER" else RED

    corner = 28
    thick = 2

    # Top-left
    cv2.line(frame, (x1, y1), (x1 + corner, y1), color, thick)
    cv2.line(frame, (x1, y1), (x1, y1 + corner), color, thick)

    # Top-right
    cv2.line(frame, (x2, y1), (x2 - corner, y1), color, thick)
    cv2.line(frame, (x2, y1), (x2, y1 + corner), color, thick)

    # Bottom-left
    cv2.line(frame, (x1, y2), (x1 + corner, y2), color, thick)
    cv2.line(frame, (x1, y2), (x1, y2 - corner), color, thick)

    # Bottom-right
    cv2.line(frame, (x2, y2), (x2 - corner, y2), color, thick)
    cv2.line(frame, (x2, y2), (x2, y2 - corner), color, thick)

    # Label
    cv2.putText(
        frame,
        f"{label} {score:.2f}",
        (x1, y1 - 12),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )
