import datetime as datetime
from sqlalchemy import Column, ForeignKey, BigInteger, DateTime
from sqlalchemy.orm import relationship
from src.schemas.resume_offer import ResumeOfferRead
from settings.database.database_connection import Base
from datetime import datetime


class ResumeOffer(Base):
    __tablename__ = "ResumeOffer"
    id = Column(BigInteger, primary_key=True)
    resume_id = Column(BigInteger, ForeignKey("Resume.id"))
    offer_id = Column(BigInteger, ForeignKey("Offer.id"))
    datetime = Column(DateTime, default=datetime.now)
    resume = relationship("Resume", lazy="selectin")
    def to_read_model(self) -> ResumeOfferRead:
        return ResumeOfferRead(
            id=self.id,
            resume=self.resume.to_read_model(),
            offer_id=self.offer_id,
            datetime=self.datetime,
        )
