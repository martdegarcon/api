from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import UserGroup
from uuid import UUID
from datetime import datetime

class UserGroupOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, group: UserGroup):
        group.created_at = datetime.utcnow()
        group.updated_at = datetime.utcnow()
        self.session.add(group)
        await self.session.commit()
        await self.session.refresh(group)
        return group

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(UserGroup).where(UserGroup.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(UserGroup).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        group = await self.get(uuid)
        if not group:
            return None
        for key, value in data.items():
            setattr(group, key, value)
        group.updated_at = datetime.utcnow()
        self.session.add(group)
        await self.session.commit()
        await self.session.refresh(group)
        return group

    async def delete(self, uuid: UUID):
        group = await self.get(uuid)
        if not group:
            return None
        await self.session.delete(group)
        await self.session.commit()
        return group 