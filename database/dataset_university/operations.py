from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import DatasetUniversity
from uuid import UUID
from datetime import datetime

class DatasetUniversityOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, university: DatasetUniversity):
        university.created_at = datetime.utcnow()
        university.updated_at = datetime.utcnow()
        self.session.add(university)
        await self.session.commit()
        await self.session.refresh(university)
        return university

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(DatasetUniversity).where(DatasetUniversity.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(DatasetUniversity).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        university = await self.get(uuid)
        if not university:
            return None
        for key, value in data.items():
            setattr(university, key, value)
        university.updated_at = datetime.utcnow()
        self.session.add(university)
        await self.session.commit()
        await self.session.refresh(university)
        return university

    async def delete(self, uuid: UUID):
        university = await self.get(uuid)
        if not university:
            return None
        await self.session.delete(university)
        await self.session.commit()
        return university 