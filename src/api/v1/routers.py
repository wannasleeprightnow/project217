from fastapi import APIRouter

from settings import settings

api_v1_router = APIRouter(
    prefix=settings.API_V1_PREFIX,
)
