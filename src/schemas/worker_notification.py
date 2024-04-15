from pydantic import BaseModel
from datetime import datetime

class WorkerNotificationRead(BaseModel):
    id: int
    is_successful: bool
    text: str
    user_id: int
    organization_id: int
    resume_offer: dict
    datetime: datetime
    is_checked: bool = False
    class from_attributes:
        orm_mode = True


class WorkerNotificationCreate(BaseModel):
    is_successful: bool
    text: str
    user_id: int
    organization_id: int
    resume_offer_id: int
    datetime: datetime
    class from_attributes:
        orm_mode = True


class WorkerNotificationUpdate(BaseModel):
    is_checked: bool = True
    class from_attributes:
        orm_mode = True