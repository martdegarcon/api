from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.ministry_position.models import MinistryPosition
from database.ministry_position.schemes import MinistryPositionCreate, MinistryPositionRead, MinistryPositionUpdate
from database.ministry_position.operations import MinistryPositionOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/ministry_positions", tags=["ministry_positions"])

@router.post("/", response_model=MinistryPositionRead, status_code=status.HTTP_201_CREATED)
async def create_position(position_data: MinistryPositionCreate, session: AsyncSession = Depends(get_session)):
    position = MinistryPosition(**position_data.dict())
    operations = MinistryPositionOperations(session)
    created_position = await operations.create(position)
    return created_position

@router.get("/", response_model=List[MinistryPositionRead], status_code=status.HTTP_200_OK)
async def read_positions(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = MinistryPositionOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=MinistryPositionRead, status_code=status.HTTP_200_OK)
async def read_position(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = MinistryPositionOperations(session)
    position = await operations.get(uuid)
    if not position:
        raise HTTPException(status_code=404, detail="MinistryPosition not found")
    return position

@router.patch("/{uuid}", response_model=MinistryPositionRead, status_code=status.HTTP_200_OK)
async def update_position(uuid: UUID, position_data: MinistryPositionUpdate, session: AsyncSession = Depends(get_session)):
    operations = MinistryPositionOperations(session)
    updated_position = await operations.update(uuid, position_data.dict(exclude_unset=True))
    if not updated_position:
        raise HTTPException(status_code=404, detail="MinistryPosition not found")
    return updated_position

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_position(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = MinistryPositionOperations(session)
    deleted_position = await operations.delete(uuid)
    if not deleted_position:
        raise HTTPException(status_code=404, detail="MinistryPosition not found")
    return None 