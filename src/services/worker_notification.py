from src.services.base import BaseService


class WorkerNotificationService(BaseService):
    async def get_entities(self, **filters):
        entities = await self.base_repo.get_all(**filters)
        entities.sort(key=lambda x: x.is_checked)
        return entities