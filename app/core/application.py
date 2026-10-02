from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.endpoints import hello


def create_api():
    api = FastAPI()

    api.include_router(hello.router, prefix='/api')
    static_dir = Path(__file__).resolve().parent.parent / 'static'
    api.mount('/', StaticFiles(directory=str(static_dir), html=True), name='frontend')

    return api
