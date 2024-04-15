from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import resume_service
from src.helper_functions.auth_handler import get_current_user
from src.schemas.resume import ResumeCreate
from src.services.resume import ResumeService

worker_resume_router = APIRouter(prefix="/v1/worker/resumes", tags=["worker / resumes"])


@worker_resume_router.get(
    "/",
    status_code=200,
    summary="Get a list of resumes of the user"
)
async def get_resumes(
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resumes = await resumes_service.get_entities(user_id=user["id"])
    return resumes


@worker_resume_router.get(
    "/{id}/",
    status_code=200,
    summary="Get resume by id"
)
async def get_resume(
    id: int,
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resume = await resumes_service.get_entity(id=id)
    if resume is None:
        raise HTTPException(status_code=404, detail="Resume not found")
    if resume.user_id != user["id"]:
        raise HTTPException(status_code=403, detail="You do not have access to this resume")
    return resume


@worker_resume_router.post(
    "/",
    status_code=201,
    summary="Create a new resume"
)
async def create_resume(
    resume: ResumeCreate,
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resume = resume.dict()
    resume["user_id"] = user["id"]
    created_resume = await resumes_service.create_entity(resume)
    return created_resume


@worker_resume_router.put(
    "/{id}/",
    status_code=200,
    summary="Update resume by id"
)
async def update_resume(
    id: int,
    resume: ResumeCreate,
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resume = resume.dict()
    resume["user_id"] = user["id"]
    updated_resume = await resumes_service.update_entity(id=id, entity=resume)
    if updated_resume is None:
        raise HTTPException(status_code=404, detail="Resume not found")
    return updated_resume


@worker_resume_router.delete(
    "/{id}/",
    status_code=200,
    summary="Delete resume by id"
)
async def delete_resume(
    id: int,
    resumes_service: Annotated[ResumeService, Depends(resume_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    resume = await resumes_service.get_entity(id=id)
    if resume is None:
        raise HTTPException(status_code=404, detail="Resume not found")
    if resume.user_id != user["id"]:
        raise HTTPException(status_code=403, detail="You do not have access to this resume")
    deleted = await resumes_service.delete_entity(id=id)
    return deleted