from sqlalchemy import select

from settings.database.database_connection import async_session
from src.services.base import BaseService
from src.models.offer import Offer


class OfferService(BaseService):
    model = Offer
    async def get_entities_in(self, ids):
        async with async_session() as session:
            stmt = select(self.model).where(self.model.disability_id.in_(ids))
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res