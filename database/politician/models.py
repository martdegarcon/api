from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from core.models import BaseOperations
from .schemes import Politician

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