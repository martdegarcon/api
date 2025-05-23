from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import User
from uuid import UUID

class UserOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User):
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(User).where(User.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(User).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        user = await self.get(uuid)
        if not user:
            return None
        for key, value in data.items():
            setattr(user, key, value)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete(self, uuid: UUID):
        user = await self.get(uuid)
        if not user:
            return None
        await self.session.delete(user)
        await self.session.commit()
        return user 