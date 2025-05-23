from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.political_party.models import PoliticalParty
from database.political_party.schemes import PoliticalPartyCreate, PoliticalPartyRead, PoliticalPartyUpdate
from database.political_party.operations import PoliticalPartyOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/political_parties", tags=["political_parties"])

@router.post("/", response_model=PoliticalPartyRead, status_code=status.HTTP_201_CREATED)
async def create_party(party_data: PoliticalPartyCreate, session: AsyncSession = Depends(get_session)):
    party = PoliticalParty(**party_data.dict())
    operations = PoliticalPartyOperations(session)
    created_party = await operations.create(party)
    return created_party

@router.get("/", response_model=List[PoliticalPartyRead], status_code=status.HTTP_200_OK)
async def read_parties(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=PoliticalPartyRead, status_code=status.HTTP_200_OK)
async def read_party(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyOperations(session)
    party = await operations.get(uuid)
    if not party:
        raise HTTPException(status_code=404, detail="PoliticalParty not found")
    return party

@router.patch("/{uuid}", response_model=PoliticalPartyRead, status_code=status.HTTP_200_OK)
async def update_party(uuid: UUID, party_data: PoliticalPartyUpdate, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyOperations(session)
    updated_party = await operations.update(uuid, party_data.dict(exclude_unset=True))
    if not updated_party:
        raise HTTPException(status_code=404, detail="PoliticalParty not found")
    return updated_party

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_party(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyOperations(session)
    deleted_party = await operations.delete(uuid)
    if not deleted_party:
        raise HTTPException(status_code=404, detail="PoliticalParty not found")
    return None 