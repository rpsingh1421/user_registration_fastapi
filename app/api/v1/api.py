from fastapi import APIRouter
from app.api.v1.endpoints import user,role

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["users"])
api_router.include_router(role.router,prefix='/role',tags=["roles"])