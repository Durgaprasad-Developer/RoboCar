# backend/api/server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router, set_camera
from vision.camera import Camera


def create_app(camera: Camera) -> FastAPI:
    app = FastAPI(title="RoboCar Brain API")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 🔥 Inject camera
    set_camera(camera)

    app.include_router(router)
    return app
