from sqlalchemy import Column, String, DateTime, ForeignKey, BigInteger, Boolean
from sqlalchemy.orm import relationship
from src.schemas.worker_notification import WorkerNotificationRead
from settings.database.database_connection import Base
from datetime import datetime


class WorkerNotification(Base):
    __tablename__ = "WorkerNotification"
    id = Column(BigInteger, primary_key=True)
    is_successful = Column(Boolean)
    text = Column(String)
    user_id = Column(BigInteger, ForeignKey('User.id'))
    organization_id = Column(BigInteger, ForeignKey('Organization.id'))
    resume_offer_id = Column(BigInteger, ForeignKey('ResumeOffer.id'))
    resume_offer = relationship("ResumeOffer", lazy="selectin")
    datetime = Column(DateTime, default=datetime.now)
    is_checked = Column(Boolean, default=False)

    def to_read_model(self) -> WorkerNotificationRead:
        return WorkerNotificationRead(
            id=self.id,
            is_successful=self.is_successful,
            text=self.text,
            user_id=self.user_id,
            organization_id=self.organization_id,
            resume_offer=self.resume_offer.to_read_model(),
            datetime=self.datetime,
            is_checked=self.is_checked,
        )
        