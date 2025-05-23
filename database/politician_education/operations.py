from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import PoliticianEducation
from uuid import UUID
from datetime import datetime

class PoliticianEducationOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, education: PoliticianEducation):
        education.created_at = datetime.utcnow()
        education.updated_at = datetime.utcnow()
        self.session.add(education)
        await self.session.commit()
        await self.session.refresh(education)
        return education

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(PoliticianEducation).where(PoliticianEducation.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(PoliticianEducation).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        education = await self.get(uuid)
        if not education:
            return None
        for key, value in data.items():
            setattr(education, key, value)
        education.updated_at = datetime.utcnow()
        self.session.add(education)
        await self.session.commit()
        await self.session.refresh(education)
        return education

    async def delete(self, uuid: UUID):
        education = await self.get(uuid)
        if not education:
            return None
        await self.session.delete(education)
        await self.session.commit()
        return education 