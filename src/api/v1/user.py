from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import user_service
from src.helper_functions.auth_handler import get_current_user
from src.services.user import UserService

user_router = APIRouter(prefix="/v1/users", tags=["users"])


@user_router.get(
    "/me/",
    status_code=200,
    summary="Get info about user"
)
async def get_user(
    user: Annotated[dict, Depends(get_current_user)],
    users_service: Annotated[UserService, Depends(user_service)]
):
    user = await users_service.get_entity(id=user["id"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

