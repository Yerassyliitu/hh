from typing import Annotated

from fastapi import APIRouter, Depends
from src.api.dependencies import disability_type_service

from src.services.disabily_type import DisabilityTypeService

disability_type_router = APIRouter(prefix="/v1/disability_types/", tags=["disability_types"])


@disability_type_router.get(
    "/",
    status_code=200,
    summary="Get a list of disability types",
)
async def get_professions(
    disability_types_service: Annotated[DisabilityTypeService, Depends(disability_type_service)],
):
    disability_types = await disability_types_service.get_entities()
    return disability_types


