from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import MinistryPosition
from uuid import UUID
from datetime import datetime

class MinistryPositionOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, position: MinistryPosition):
        position.created_at = datetime.utcnow()
        position.updated_at = datetime.utcnow()
        self.session.add(position)
        await self.session.commit()
        await self.session.refresh(position)
        return position

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(MinistryPosition).where(MinistryPosition.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(MinistryPosition).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        position = await self.get(uuid)
        if not position:
            return None
        for key, value in data.items():
            setattr(position, key, value)
        position.updated_at = datetime.utcnow()
        self.session.add(position)
        await self.session.commit()
        await self.session.refresh(position)
        return position

    async def delete(self, uuid: UUID):
        position = await self.get(uuid)
        if not position:
            return None
        await self.session.delete(position)
        await self.session.commit()
        return position 