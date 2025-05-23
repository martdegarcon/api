from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from core.models import BaseOperations
from .schemes import Politician
from uuid import UUID

class PoliticianOperations(BaseOperations):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, politician: Politician) -> tuple[bool, str]:
        """
        Create a new politician in the database
        
        :param politician: Politician object to create
        :return: tuple of (success status, message)
        """
        status, message = await self._validate_politician(politician)
        if status:
            await self._create_one(politician, "Politician created successfully")
        return status, message

    async def get_politicians(self, skip: int = 0, limit: int = 10) -> list[Politician]:
        """
        Get list of politicians with pagination
        
        :param skip: Number of records to skip
        :param limit: Maximum number of records to return
        :return: List of Politician objects
        """
        query = select(Politician).offset(skip).limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_politician(self, uuid: UUID) -> Politician:
        query = select(Politician).where(Politician.uuid == uuid)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def update_politician(self, uuid: UUID, data: dict) -> Politician:
        politician = await self.get_politician(uuid)
        if not politician:
            return None
        for key, value in data.items():
            setattr(politician, key, value)
        self.session.add(politician)
        await self.session.commit()
        await self.session.refresh(politician)
        return politician

    async def delete_politician(self, uuid: UUID) -> Politician:
        politician = await self.get_politician(uuid)
        if not politician:
            return None
        await self.session.delete(politician)
        await self.session.commit()
        return politician

    @staticmethod
    async def _validate_politician(politician: Politician) -> tuple[bool, str]:
        """
        Validate politician data before creation
        
        :param politician: Politician object to validate
        :return: tuple of (validation status, message)
        """
        if not politician.name:
            return False, "Name is required"
        return True, "Validation successful" 