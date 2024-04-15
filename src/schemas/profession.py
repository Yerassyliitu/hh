from pydantic import BaseModel


class ProfessionCreate(BaseModel):
    name: str

    class from_attributes:
        orm_mode = True


class ProfessionRead(BaseModel):
    id: int
    name: str

    class from_attributes:
        orm_mode = True