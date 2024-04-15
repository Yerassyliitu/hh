from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import offer_service, resume_service
from src.helper_functions.auth_handler import get_current_user
from src.services.offer import OfferService
from src.services.resume import ResumeService

worker_offer_router = APIRouter(prefix="/v1/worker/offers", tags=["worker / offers"])


@worker_offer_router.get(
    "/",
    status_code=200,
    summary="Get a list of offers for user"
)
async def get_offers(
    offers_service: Annotated[OfferService, Depends(offer_service)],
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resumes = await resumes_service.get_entities(user_id=user["id"])
    disability_types = [resume["disability_id"] for resume in resumes]
    offers = await offers_service.get_entities_in(ids=disability_types)
    return offers


@worker_offer_router.get(
    "/{id}",
    status_code=200,
    summary="Get an offer by id"
)
async def get_offer(
    id: int,
    offers_service: Annotated[OfferService, Depends(offer_service)]
):
    offer = await offers_service.get_entity(id=id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer