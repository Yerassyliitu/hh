from src.repositories.all_repositories import *
from src.services.user import UserService
from src.services.disabily_type import DisabilityTypeService
from src.services.experience import ExperiencService
from src.services.offer import OfferService
from src.services.organization import OrganizationService
from src.services.profession import ProfessionService
from src.services.resume import ResumeService
from src.services.worker_notification import WorkerNotificationService


def user_service():
    return UserService(UserRepository())


def disability_type_service():
    return DisabilityTypeService(Disability_TypeRepository())


def experience_service():
    return ExperiencService(ExperienceRepository())


def offer_service():
    return OfferService(OfferRepository())


def organization_service():
    return OrganizationService(OrganizationRepository())


def profession_service():
    return ProfessionService(ProfessionRepository())


def resume_service():
    return ResumeService(ResumeRepository())


def worker_notification_service():
    return WorkerNotificationService(WorkerNotificationRepository())

