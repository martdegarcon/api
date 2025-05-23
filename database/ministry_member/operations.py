from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import MinistryMember
from uuid import UUID
from datetime import datetime

class MinistryMemberOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, member: MinistryMember):
        member.created_at = datetime.utcnow()
        member.updated_at = datetime.utcnow()
        self.session.add(member)
        await self.session.commit()
        await self.session.refresh(member)
        return member

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(MinistryMember).where(MinistryMember.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(MinistryMember).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        member = await self.get(uuid)
        if not member:
            return None
        for key, value in data.items():
            setattr(member, key, value)
        member.updated_at = datetime.utcnow()
        self.session.add(member)
        await self.session.commit()
        await self.session.refresh(member)
        return member

    async def delete(self, uuid: UUID):
        member = await self.get(uuid)
        if not member:
            return None
        await self.session.delete(member)
        await self.session.commit()
        return member 