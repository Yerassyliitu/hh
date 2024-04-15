from pydantic import BaseModel


class DisabilityTypeCreate(BaseModel):
    id: int



class DisabilityTypeRead(BaseModel):
    id: int
    name: str

