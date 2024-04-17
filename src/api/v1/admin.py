from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import RedirectResponse
from src.api.dependencies import worker_regular_alert_service
from src.helper_functions.auth_handler import get_current_user

from src.services.worker_regular_alert import WorkerRegularAlertService


admin = APIRouter(prefix="/v1/admin", tags=["admin-panel"])





@admin.get("/")
async def redirect_to_url():  
    target_url = "https://adminflask.up.railway.app/admin/"
    return RedirectResponse(url=target_url)