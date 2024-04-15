from sqlalchemy import Column, String, BigInteger
from src.schemas.disabily_type import DisabilityTypeRead
from settings.database.database_connection import Base



class DisabilityType(Base):
    __tablename__ = "DisabilityType"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    def to_read_model(self) -> DisabilityTypeRead:
        return DisabilityTypeRead(
            id=self.id,
            name=self.name,
        )