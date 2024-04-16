from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import worker_regular_alert_service
from src.helper_functions.auth_handler import get_current_user

from src.services.worker_regular_alert import WorkerRegularAlertService


from src.celery.tasks import test

worker_regular_alert_router = APIRouter(prefix="/v1/worker/regular-alert", tags=["worker / regular-alert"])

@worker_regular_alert_router.post(
    "/",
    status_code=201,
    summary="Create Worker Regular Alert"
)
async def create_worker_regular_alert(
    worker_regular_alert_service: Annotated[WorkerRegularAlertService, Depends(worker_regular_alert_service)],
    user: Annotated[dict, Depends(get_current_user)]
):
    worker_regular_alert_check = await worker_regular_alert_service.get_entity(user_id=user['id'])
    if worker_regular_alert_check:
        raise HTTPException(status_code=400, detail="Вы уже подписанны на рассылку")
    worker_regular_alert_id= await worker_regular_alert_service.create_entity({'user_id': user['id']})
    if worker_regular_alert_id:
        return worker_regular_alert_id
    else:
        raise HTTPException(status_code=400, detail="У нас не получилось подписать вас на рассылку :(")

@worker_regular_alert_router.delete(
    "/{id}/",
    status_code=204,
    summary="Delete Worker Regular Alert"
)
async def delete_regular_alert(
    id: int,
    worker_regular_alert_service: Annotated[WorkerRegularAlertService, Depends(worker_regular_alert_service)],
):
    regular_alert = await worker_regular_alert_service.delete_entity(id=id)
    if regular_alert:
        return {}
    else:
        raise HTTPException(status_code=400, detail="Вы уже отписались от нашей рассылки")
    


    
    
