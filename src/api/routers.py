from .v1.auth import auth_router
from .v1.profession import profession_router
from .v1.user import user_router
from .v1.worker.offer import worker_offer_router
from .v1.worker.resume import worker_resume_router
from .v1.worker.experience import worker_experience_router

all_routers = [
    auth_router,
    user_router,
    profession_router,
    worker_offer_router,
    worker_resume_router,
    worker_experience_router,
]
