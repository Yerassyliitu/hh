from sqlalchemy import Column, String, BigInteger
from src.schemas.organization import OrganizationRead
from settings.database.database_connection import Base



class Organization(Base):
    __tablename__ = "Organization"
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    description = Column(String)
    def to_read_model(self) -> OrganizationRead:
        return OrganizationRead(
            id=self.id,
            name=self.name,
            description=self.description,
        )   