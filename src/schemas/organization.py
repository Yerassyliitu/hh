from pydantic import BaseModel, Field


class OrganizationCreate(BaseModel):
    name: str = Field("...", max_length=30)
    description: str = Field(max_length=500)

    class from_attributes:
        orm_mode = True


class OrganizationRead(BaseModel):
    id: int
    name: str = Field("...", max_length=30)
    description: str = Field(max_length=500)

    class from_attributes:
        orm_mode = True