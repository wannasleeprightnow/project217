import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.routers import api_v1_router
from middlewares import SecurityHeadersMiddleware
from settings import settings

logger = logging.getLogger(__name__)

app = FastAPI(
    debug=True,
    title="project217",
)

app.include_router(api_v1_router)

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
