from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import worker_notification_service
from src.helper_functions.auth_handler import get_current_user
from src.schemas.worker_notification import  WorkerNotificationUpdate
from src.services.worker_notification import WorkerNotificationService


worker_notification_router = APIRouter(prefix="/v1/worker/notifications", tags=["worker / notifications"])

@worker_notification_router.get(
    "/",
    status_code=200,
    summary="Get a list of notifications",
)
async def get_notifications(
    worker_notifications_service: Annotated[WorkerNotificationService, Depends(worker_notification_service)],
    user: Annotated[dict, Depends(get_current_user)],
):
    worker_notifications = await worker_notifications_service.get_entities(user_id=user['id'])
    return worker_notifications


@worker_notification_router.get(
    "/{id}/",
    status_code=200,
    summary="Read and Make the notification checked",
)
async def update_notification(
    id: int,
    worker_notifications_service: Annotated[WorkerNotificationService, Depends(worker_notification_service)],
    user: Annotated[dict, Depends(get_current_user)],
):
    worker_notification = await worker_notifications_service.get_entity(id=id)
    if not worker_notification:
        raise HTTPException(status_code=400, detail="We can not find this notification by id")
    if worker_notification.user_id != user['id']:
        raise HTTPException(status_code=403, detail="You do not have access to this notification")
    
    updated_notification = await worker_notifications_service.update_entity(id=id, entity=WorkerNotificationUpdate)
    if updated_notification:
        return updated_notification
    return HTTPException(status_code=400, detail="Something went wrong :(. Maybe an attack helicopter could help you?")
