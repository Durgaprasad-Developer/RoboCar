import cv2
import numpy as np
from backend.vision.camera import Camera

cam = Camera()

def nothing(x):
    pass

cv2.namedWindow("HSV Tuner")

cv2.createTrackbar("H Min", "HSV Tuner", 0, 179, nothing)
cv2.createTrackbar("H Max", "HSV Tuner", 179, 179, nothing)
cv2.createTrackbar("S Min", "HSV Tuner", 0, 255, nothing)
cv2.createTrackbar("S Max", "HSV Tuner", 255, 255, nothing)
cv2.createTrackbar("V Min", "HSV Tuner", 0, 255, nothing)
cv2.createTrackbar("V Max", "HSV Tuner", 255, 255, nothing)

while True:
    frame = cam.get_frame()
    if frame is None:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("H Min", "HSV Tuner")
    h_max = cv2.getTrackbarPos("H Max", "HSV Tuner")
    s_min = cv2.getTrackbarPos("S Min", "HSV Tuner")
    s_max = cv2.getTrackbarPos("S Max", "HSV Tuner")
    v_min = cv2.getTrackbarPos("V Min", "HSV Tuner")
    v_max = cv2.getTrackbarPos("V Max", "HSV Tuner")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("LOWER_HSV =", lower)
        print("UPPER_HSV =", upper)
        break

cam.release()
cv2.destroyAllWindows()