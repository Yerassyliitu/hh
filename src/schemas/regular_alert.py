from pydantic import BaseModel, EmailStr


class RegularAlertRead(BaseModel):
    id: int
    email: EmailStr
    period: str
    class from_attributes:
        orm_mode = True

class RegularAlertCreate(BaseModel):
    email: EmailStr
    period: str = "daily"
    class from_attributes:
        orm_mode = True
