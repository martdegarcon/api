from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import Government
from uuid import UUID
from datetime import datetime

class GovernmentOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, government: Government):
        government.created_at = datetime.utcnow()
        government.updated_at = datetime.utcnow()
        self.session.add(government)
        await self.session.commit()
        await self.session.refresh(government)
        return government

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(Government).where(Government.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(Government).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        government = await self.get(uuid)
        if not government:
            return None
        for key, value in data.items():
            setattr(government, key, value)
        government.updated_at = datetime.utcnow()
        self.session.add(government)
        await self.session.commit()
        await self.session.refresh(government)
        return government

    async def delete(self, uuid: UUID):
        government = await self.get(uuid)
        if not government:
            return None
        await self.session.delete(government)
        await self.session.commit()
        return government 