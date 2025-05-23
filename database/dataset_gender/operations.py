from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import DatasetGender
from uuid import UUID
from datetime import datetime

class DatasetGenderOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, gender: DatasetGender):
        gender.created_at = datetime.utcnow()
        gender.updated_at = datetime.utcnow()
        self.session.add(gender)
        await self.session.commit()
        await self.session.refresh(gender)
        return gender

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(DatasetGender).where(DatasetGender.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(DatasetGender).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        gender = await self.get(uuid)
        if not gender:
            return None
        for key, value in data.items():
            setattr(gender, key, value)
        gender.updated_at = datetime.utcnow()
        self.session.add(gender)
        await self.session.commit()
        await self.session.refresh(gender)
        return gender

    async def delete(self, uuid: UUID):
        gender = await self.get(uuid)
        if not gender:
            return None
        await self.session.delete(gender)
        await self.session.commit()
        return gender 