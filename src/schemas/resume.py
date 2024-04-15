from pydantic import BaseModel, Field, conint
from datetime import date
from typing import List

from .experience import ExperienceRead


class ResumeCreate(BaseModel):
    firstname: str
    lastname: str
    region: str
    phone: str
    degree: str
    gender: str
    birthday: date
    profession_id: int
    disability_type_id: int

    class from_attributes:
        orm_mode = True




class ResumeRead(BaseModel):
    id: int
    firstname: str
    lastname: str
    region: str
    phone: str
    degree: str
    gender: str
    birthday: date
    profession: dict
    disability_type: dict
    experiences: List[ExperienceRead]

    class from_attributes:
        orm_mode = True


