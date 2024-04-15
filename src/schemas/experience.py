from pydantic import BaseModel, Field
from datetime import date


class ExperienceUpdate(BaseModel):
    company_name: str = Field("...", max_length=30)
    description: str = Field("...", max_length=500)
    start_date: date
    finish_date: date = None
    is_work_now: bool

    class from_attributes:
        orm_mode = True


class ExperienceCreate(BaseModel):
    company_name: str = Field("...", max_length=30)
    description: str = Field("...", max_length=500)
    start_date: date
    finish_date: date = None
    is_work_now: bool
    resume_id: int
    class from_attributes:
        orm_mode = True



class ExperienceRead(ExperienceCreate):
    id: int
    company_name: str = Field("...", max_length=30)
    description: str = Field("...", max_length=500)
    start_date: date
    finish_date: date = None
    is_work_now: bool
    resume_id: int

    class from_attributes:
        orm_mode = True