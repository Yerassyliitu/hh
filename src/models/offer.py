from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from src.schemas.offer import OfferRead
from settings.database.database_connection import Base



class Offer(Base):
    __tablename__ = "Offer"
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    description = Column(String)
    profession_id = Column(BigInteger, ForeignKey("Profession.id"))
    disability_id = Column(BigInteger, ForeignKey("DisabilityType.id"))
    organization_id = Column(BigInteger, ForeignKey("Organization.id"))
    organization = relationship("Organization", lazy="selectin")
    disability_type = relationship("DisabilityType", lazy="selectin")
    profession = relationship("Profession", lazy="selectin")
    def to_read_model(self) -> OfferRead:
        return OfferRead(
            id=self.id,
            name=self.name,
            description=self.description,
            profession={
                "id": self.profession.id,
                "name": self.profession.name
            },
            disability_type={
                "id": self.disability_type.id,
                "name": self.disability_type.name
            },
            organization={
                "id": self.organization.id,
                "name": self.organization.name
            }
        )
