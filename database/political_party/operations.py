from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import PoliticalParty
from uuid import UUID
from datetime import datetime

class PoliticalPartyOperations:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, party: PoliticalParty):
        party.created_at = datetime.utcnow()
        party.updated_at = datetime.utcnow()
        self.session.add(party)
        await self.session.commit()
        await self.session.refresh(party)
        return party

    async def get(self, uuid: UUID):
        result = await self.session.execute(select(PoliticalParty).where(PoliticalParty.uuid == uuid))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 10):
        result = await self.session.execute(select(PoliticalParty).offset(skip).limit(limit))
        return result.scalars().all()

    async def update(self, uuid: UUID, data: dict):
        party = await self.get(uuid)
        if not party:
            return None
        for key, value in data.items():
            setattr(party, key, value)
        party.updated_at = datetime.utcnow()
        self.session.add(party)
        await self.session.commit()
        await self.session.refresh(party)
        return party

    async def delete(self, uuid: UUID):
        party = await self.get(uuid)
        if not party:
            return None
        await self.session.delete(party)
        await self.session.commit()
        return party 