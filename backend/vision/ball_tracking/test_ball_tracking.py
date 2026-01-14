import cv2
import time
import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(ROOT)

from vision.camera import Camera
from vision.ball_tracking.ball_track import BallTracker

cam = Camera()
tracker = BallTracker()

print("🧪 Ball Tracking Test (press q to quit)")

while True:
    frame = cam.get_frame()
    if frame is None:
        break

    frame, center = tracker.run(frame)

    if center:
        print(f"[{time.time():.3f}] 🎯 Ball center: {center}")

    cv2.imshow("Ball Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()