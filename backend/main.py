# backend/main.py

import threading
import uvicorn

from core.loop import run_brain_loop
from api.server import create_app
from manual_input.keyboard import start_keyboard
from vision.camera import Camera


def start_brain(camera: Camera):
    run_brain_loop(camera)


if __name__ == "__main__":
    # 🔥 ONE camera for everything
    camera = Camera()

    # Brain loop thread
    brain_thread = threading.Thread(
        target=start_brain,
        args=(camera,),
        daemon=True,
    )
    brain_thread.start()

    # Keyboard manual input
    start_keyboard()

    # API server (blocking)
    app = create_app(camera)
    uvicorn.run(app, host="0.0.0.0", port=8000)
