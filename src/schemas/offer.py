from pydantic import BaseModel, Field


class OfferUpdate(BaseModel):
    name: str = Field("...", max_length=30)
    description: str = Field("...", max_length=500)
    profession_id: int = None
    disability_id: int = None

    class from_attributes:
        orm_mode = True


class OfferCreate(OfferUpdate):
    name: str = Field("...", max_length=30)
    description: str = Field("...", max_length=500)
    profession_id: int
    organization_id: int
    disability_id: int
    class from_attributes:
        orm_mode = True


class OfferRead(OfferUpdate):
    id: int
    name: str = Field("...", max_length=30)
    description: str = Field("...", max_length=500)
    profession: dict
    disability_type: dict
    organization: dict

    class from_attributes:
        orm_mode = True