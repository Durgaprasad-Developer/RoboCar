import cv2
from camera import Camera

def main():
    cam = Camera(camera_id=0)

    while True:
        frame = cam.get_frame()
        if frame is None:
            print("❌ No frame received")
            break

        cv2.imshow("Robot Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
