from fastapi import FastAPI

from api.v1.routers import api_v1_root_router


def init_routers(app: FastAPI) -> None:
    app.include_router(api_v1_root_router)
