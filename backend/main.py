# backend/main.py

import threading
import uvicorn

from core.loop import run_brain_loop
from api.server import create_app
from manual_input.keyboard import start_keyboard



def start_brain():
    run_brain_loop()


if __name__ == "__main__":
    # Start robot brain loop (NON-daemon)
    brain_thread = threading.Thread(target=start_brain)
    brain_thread.start()
    start_keyboard()


    # Start API server (blocking, main thread)
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
