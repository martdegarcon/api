from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import Ministry
from uuid import UUID
from datetime import datetime

class MinistryOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, ministry: Ministry):
        ministry.created_at = datetime.utcnow()
        ministry.updated_at = datetime.utcnow()
        self.session.add(ministry)
        await self.session.commit()
        await self.session.refresh(ministry)
        return ministry

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(Ministry).where(Ministry.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(Ministry).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        ministry = await self.get(uuid)
        if not ministry:
            return None
        for key, value in data.items():
            setattr(ministry, key, value)
        ministry.updated_at = datetime.utcnow()
        self.session.add(ministry)
        await self.session.commit()
        await self.session.refresh(ministry)
        return ministry

    async def delete(self, uuid: UUID):
        ministry = await self.get(uuid)
        if not ministry:
            return None
        await self.session.delete(ministry)
        await self.session.commit()
        return ministry 