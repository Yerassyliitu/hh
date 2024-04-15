from sqlalchemy import Column, String, ForeignKey, BigInteger, Date, Boolean
from src.schemas.experience import ExperienceRead
from settings.database.database_connection import Base



class Experience(Base):
    __tablename__ = "Experience"
    id = Column(BigInteger, primary_key=True)
    company_name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    finish_date = Column(Date)
    is_work_now = Column(Boolean)
    resume_id = Column(BigInteger, ForeignKey("Resume.id"))
    def to_read_model(self) -> ExperienceRead:
        return ExperienceRead(
            id=self.id,
            company_name=self.company_name,
            description=self.decription,
            start_date=self.start_date,
            finish_date=self.finish_date,
            is_work_now=self.is_work_now,
            resume_id=self.resume_id
        )  