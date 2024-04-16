from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from src.schemas.worker_regular_alert import WorkerRegularAlertRead
from settings.database.database_connection import Base


class WorkerRegularAlert(Base):
    __tablename__ = "WorkerRegularAlert"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('User.id'))
    user = relationship('User', lazy="selectin")
    def to_read_model(self) -> WorkerRegularAlertRead:
        return WorkerRegularAlertRead(
            id=self.id,
            user={"email": self.user.email},
        )
