from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import experience_service, resume_service
from src.helper_functions.auth_handler import get_current_user
from src.schemas.experience import ExperienceCreate
from src.services.experience import ExperiencService
from src.services.resume import ResumeService

worker_experience_router = APIRouter(prefix="/v1/worker/experiences", tags=["worker / experience"])


@worker_experience_router.get(
    "/{id}/",
    status_code=200,
    summary="Get experience by id"
)
async def get_experience(
    id: int,
    experiences_service: Annotated[ExperiencService, Depends(experience_service)],
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    experience = await experiences_service.get_entity(id=id)
    resume = await resumes_service.get_entity(id=experience.resume_id)
    if resume.user_id != user["id"]:
        raise HTTPException(status_code=403, detail="You do not have access to this experience")
    if experience is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    return experience


@worker_experience_router.post(
    "/",
    status_code=201,
    summary="Create a new experience"
)
async def create_experience(
    experience: ExperienceCreate,
    experiences_service: Annotated[ExperiencService, Depends(experience_service)],
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resume = await resumes_service.get_entity(id=experience.resume_id)
    if resume.user_id != user["id"]:
        raise HTTPException(status_code=403, detail="You do not have access to this resume")
    created_experience = await experiences_service.create_entity(experience)
    if created_experience is None:
        raise HTTPException(status_code=404, detail="Resume not found")
    return created_experience


@worker_experience_router.put(
    "/{id}/",
    status_code=200,
    summary="Update experience by id"
)
async def update_experience(
    id: int,
    experience: ExperienceCreate,
    experiences_service: Annotated[ExperiencService, Depends(experience_service)],
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resume = await resumes_service.get_entity(id=experience.resume_id)
    if resume.user_id != user["id"]:
        raise HTTPException(status_code=403, detail="You do not have access to this resume")
    updated_experience = await experiences_service.update_entity(id=id, entity=experience)
    if updated_experience is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    return updated_experience


@worker_experience_router.delete(
    "/{id}/",
    status_code=204,
    summary="Delete experience by id"
)
async def delete_experience(
    id: int,
    experiences_service: Annotated[ExperiencService, Depends(experience_service)],
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    experience = await experiences_service.get_entity(id=id)
    if experience is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    resume = await resumes_service.get_entity(id=experience.resume_id)
    if resume.user_id != user["id"]:
        raise HTTPException(status_code=403, detail="You do not have access to this resume")
    deleted_experience = await experiences_service.delete_entity(id=id)
    if deleted_experience is None:
        raise HTTPException(status_code=404, detail="Experience not found")
    return deleted_experience