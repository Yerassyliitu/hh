from pydantic import BaseModel
from datetime import date



class ResumeOfferCreate(BaseModel):
    resume_id: int
    offer_id: int
    class from_attributes:
        orm_mode = True


class ResumeOfferRead(BaseModel):
    id: int
    resume: dict
    offer_id: int
    datetime: date
    class from_attributes:
        orm_mode = True