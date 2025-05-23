from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.politician.schemes import Politician, PoliticianCreate
from database.politician.models import PoliticianOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/politicians", tags=["politicians"])

@router.post("/", response_model=Politician, status_code=status.HTTP_201_CREATED)
async def create_politician(politician_data: PoliticianCreate, session: AsyncSession = Depends(get_session)):
    politician = Politician(**politician_data.dict())
    operations = PoliticianOperations(session)
    status_, message = await operations.create(politician)
    if not status_:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT if "already exists" in message.lower() 
            else status.HTTP_400_BAD_REQUEST,
            detail=message
        )
    return politician

@router.get("/", response_model=List[Politician], status_code=status.HTTP_200_OK)
async def read_politicians(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = PoliticianOperations(session)
    return await operations.get_politicians(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=Politician, status_code=status.HTTP_200_OK)
async def read_politician(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticianOperations(session)
    politician = await operations.get_politician(uuid)
    if not politician:
        raise HTTPException(status_code=404, detail="Politician not found")
    return politician

@router.patch("/{uuid}", response_model=Politician, status_code=status.HTTP_200_OK)
async def update_politician(uuid: UUID, politician_data: PoliticianCreate, session: AsyncSession = Depends(get_session)):
    operations = PoliticianOperations(session)
    updated_politician = await operations.update_politician(uuid, politician_data.dict(exclude_unset=True))
    if not updated_politician:
        raise HTTPException(status_code=404, detail="Politician not found")
    return updated_politician

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_politician(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticianOperations(session)
    deleted_politician = await operations.delete_politician(uuid)
    if not deleted_politician:
        raise HTTPException(status_code=404, detail="Politician not found")
    return None 