from typing import Annotated

from fastapi import APIRouter, Depends
from src.api.dependencies import profession_service
from src.helper_functions.auth_handler import get_current_user

from src.services.profession import ProfessionService
from src.schemas.profession import ProfessionCreate

profession_router = APIRouter(prefix="/v1/professions", tags=["professions"])


@profession_router.get(
    "/",
    status_code=200,
    summary="Get a list of professions"
)
async def get_professions(
    professions_service: Annotated[ProfessionService, Depends(profession_service)],
):
    professions = await professions_service.get_entities()
    return professions


@profession_router.post(
    "/",
    status_code=201,
    summary="Create profession"
)
async def create_profession(
    professions_service: Annotated[ProfessionService, Depends(profession_service)],
    profession: ProfessionCreate,
    user: Annotated[dict, Depends(get_current_user)],
):
    profession = await professions_service.create_entity(entity=profession)
    return profession


