from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import DatasetProvince
from uuid import UUID
from datetime import datetime

class DatasetProvinceOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, province: DatasetProvince):
        province.created_at = datetime.utcnow()
        province.updated_at = datetime.utcnow()
        self.session.add(province)
        await self.session.commit()
        await self.session.refresh(province)
        return province

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(DatasetProvince).where(DatasetProvince.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(DatasetProvince).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        province = await self.get(uuid)
        if not province:
            return None
        for key, value in data.items():
            setattr(province, key, value)
        province.updated_at = datetime.utcnow()
        self.session.add(province)
        await self.session.commit()
        await self.session.refresh(province)
        return province

    async def delete(self, uuid: UUID):
        province = await self.get(uuid)
        if not province:
            return None
        await self.session.delete(province)
        await self.session.commit()
        return province 