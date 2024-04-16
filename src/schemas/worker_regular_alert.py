from pydantic import BaseModel
from typing import Dict


class WorkerRegularAlertRead(BaseModel):
    id: int
    user: Dict
    class from_attributes:
        orm_mode = True


