from fastapi.routing import APIRouter

from src.api.system.views import router as system
from src.api.user.views import router as user

api_router = APIRouter()
api_router.include_router(user, prefix="/user", tags=["user"])
api_router.include_router(system, prefix="", tags=["default"])
