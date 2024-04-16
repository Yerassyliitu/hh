from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from src.api.dependencies import regular_alert_service, worker_regular_alert_service

from src.services.regular_alert import RegularAlertService
from src.schemas.regular_alert import RegularAlertCreate


from src.celery.tasks import test

regular_alert_router = APIRouter(prefix="/v1/regular-alert", tags=["regular-alert"])


@regular_alert_router.post(
    "/",
    status_code=201,
    summary="Create Regular Alert"
)
async def create_regular_alert(
    regular_alert: RegularAlertCreate,
    regular_alert_service: Annotated[RegularAlertService, Depends(regular_alert_service)]
):
    regular_alert_check = await regular_alert_service.get_entity(email=regular_alert.email)
    if regular_alert_check:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже подписан на рассылку")
    regular_alert_id= await regular_alert_service.create_entity(regular_alert)
    if regular_alert_id:
        return regular_alert_id
    else:
        raise HTTPException(status_code=400, detail="У нас не получилось подписать вас на рассылку :(")
    

@regular_alert_router.delete(
    "/{id}/",
    status_code=204,
    summary="Delete Regular Alert"
)
async def delete_regular_alert(
    id: int,
    regular_alert_service: Annotated[RegularAlertService, Depends(regular_alert_service)],
):
    regular_alert = await regular_alert_service.delete_entity(id=id)
    if regular_alert:
        return {}
    else:
        raise HTTPException(status_code=400, detail="Вы уже отписались от нашей рассылки")
    


    
    
