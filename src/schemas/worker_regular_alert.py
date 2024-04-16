from pydantic import BaseModel


class WorkerRegularAlertRead(BaseModel):
    id: int
    user: dict
    class from_attributes:
        orm_mode = True


