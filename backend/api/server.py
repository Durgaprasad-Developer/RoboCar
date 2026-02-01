# backend/api/server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router


def create_app() -> FastAPI:
    app = FastAPI(title="RoboCar Brain API")

    # ✅ CORS FIX (TB-12)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # React dev server
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)
    return app
