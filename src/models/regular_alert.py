from sqlalchemy import Column, String, BigInteger
from src.schemas.regular_alert import RegularAlertRead
from settings.database.database_connection import Base


class RegularAlert(Base):
    __tablename__ = "RegularAlert"
    id = Column(BigInteger, primary_key=True)
    email = Column(String)
    period = Column(String)

    def to_read_model(self) -> RegularAlertRead:
        return RegularAlertRead(
            id=self.id,
            email=self.email,
            period=self.period,
        )
