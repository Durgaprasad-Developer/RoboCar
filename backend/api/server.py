#backend/api/server.py

from fastapi import FastAPI
from api.routes import router

def create_app() -> FastAPI:
    app = FastAPI(title="RoboCar Brain API")

    app.include_router(router)

    return app