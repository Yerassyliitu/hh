from sqlalchemy import Column, String, BigInteger
from src.schemas.profession import ProfessionRead
from settings.database.database_connection import Base


class Profession(Base):
    __tablename__ = "Profession"
    id = Column(BigInteger, primary_key=True)
    name = Column(String)

    def to_read_model(self) -> ProfessionRead:
        return ProfessionRead(
            id=self.id,
            name=self.name,
        )
