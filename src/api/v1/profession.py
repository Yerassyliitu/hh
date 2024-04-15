from typing import Annotated

from fastapi import APIRouter, Depends
from src.api.dependencies import profession_service

from src.services.profession import ProfessionService

profession_router = APIRouter(prefix="/v1/professions", tags=["profession"])


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


