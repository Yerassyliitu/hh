from sqlalchemy import Column, String, ForeignKey, BigInteger, Date
from sqlalchemy.orm import relationship
from src.schemas.resume import ResumeRead
from settings.database.database_connection import Base


class Resume(Base):
    __tablename__ = "Resume"
    id = Column(BigInteger, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String)
    region = Column(String)
    birthday = Column(Date)
    phone = Column(String)
    degree = Column(String)
    profession_id = Column(BigInteger, ForeignKey("Profession.id"))
    disability_id = Column(BigInteger, ForeignKey("DisabilityType.id"))
    user_id = Column(BigInteger, ForeignKey("User.id"))
    profession = relationship("Profession", lazy="selectin")
    disability_type = relationship("DisabilityType", lazy="selectin")

    experiences = relationship("Experience")
    def to_read_model(self) -> ResumeRead:
        return ResumeRead(
            id=self.id,
            firstname=self.firstname,
            lastname=self.lastname,
            region=self.region,
            phone=self.phone,
            degree=self.degree,
            gender=self.gender,
            birthday=self.birthday,
            profession={"id": self.profession.id, "name": self.profession.name},
            disability_type={"id": self.disability_type.id, "name": self.disability_type.name},
            experiences=[experience.to_read_model() for experience in self.experiences]
        )
