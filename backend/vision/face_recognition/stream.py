import cv2
import time
from flask import Flask, Response
from threading import Lock

class VideoStreamer:
    def __init__(self, host="0.0.0.0", port=5000):
        self.app = Flask(__name__)
        self.frame = None
        self.lock = Lock()
        self.host = host
        self.port = port

        @self.app.route("/")
        def index():
            return """
            <html>
            <head><title>Robo Face Recognition</title></head>
            <body style="background:black;text-align:center;">
                <h2 style="color:white;">🤖 Robo Face Recognition</h2>
                <img src="/video" width="720"/>
            </body>
            </html>
            """

        @self.app.route("/video")
        def video():
            return Response(
                self.generate(),
                mimetype="multipart/x-mixed-replace; boundary=frame"
            )

    def update(self, frame):
        with self.lock:
            self.frame = frame.copy()

    def generate(self):
        while True:
            with self.lock:
                if self.frame is None:
                    continue

                ret, buffer = cv2.imencode(
                    ".jpg",
                    self.frame,
                    [int(cv2.IMWRITE_JPEG_QUALITY), 70]
                )

            if not ret:
                continue

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n"
                + buffer.tobytes()
                + b"\r\n"
            )

            time.sleep(0.03)

    def start(self):
        self.app.run(host=self.host, port=self.port, threaded=True)
