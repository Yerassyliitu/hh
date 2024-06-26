from src.models.user import User
from src.models.disability_type import DisabilityType
from src.models.experience import Experience
from src.models.resume_offer import ResumeOffer
from src.models.offer import Offer
from src.models.organization import Organization
from src.models.profession import Profession
from src.models.resume import Resume
from src.models.worker_notification import WorkerNotification
from src.models.regular_alert import RegularAlert
from src.models.worker_regular_alert import WorkerRegularAlert

from src.repositories.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User


class Disability_TypeRepository(SQLAlchemyRepository):
    model = DisabilityType


class ExperienceRepository(SQLAlchemyRepository):
    model = Experience


class OfferRepository(SQLAlchemyRepository):
    model = Offer


class OrganizationRepository(SQLAlchemyRepository):
    model = Organization

    
class ProfessionRepository(SQLAlchemyRepository):
    model = Profession


class ResumeRepository(SQLAlchemyRepository):
    model = Resume


class ResumeOfferRepository(SQLAlchemyRepository):
    model = ResumeOffer


class WorkerNotificationRepository(SQLAlchemyRepository):
    model = WorkerNotification


class RegularAlertRepository(SQLAlchemyRepository):
    model = RegularAlert


class WorkerRegularAlertRepository(SQLAlchemyRepository):
    model = WorkerRegularAlert
