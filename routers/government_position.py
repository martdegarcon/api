from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.government_position.models import GovernmentPosition
from database.government_position.schemes import GovernmentPositionCreate, GovernmentPositionRead, GovernmentPositionUpdate
from database.government_position.operations import GovernmentPositionOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/government_positions", tags=["government_positions"])

@router.post("/", response_model=GovernmentPositionRead, status_code=status.HTTP_201_CREATED)
async def create_position(position_data: GovernmentPositionCreate, session: AsyncSession = Depends(get_session)):
    position = GovernmentPosition(**position_data.dict())
    operations = GovernmentPositionOperations(session)
    created_position = await operations.create(position)
    return created_position

@router.get("/", response_model=List[GovernmentPositionRead], status_code=status.HTTP_200_OK)
async def read_positions(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = GovernmentPositionOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=GovernmentPositionRead, status_code=status.HTTP_200_OK)
async def read_position(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = GovernmentPositionOperations(session)
    position = await operations.get(uuid)
    if not position:
        raise HTTPException(status_code=404, detail="GovernmentPosition not found")
    return position

@router.patch("/{uuid}", response_model=GovernmentPositionRead, status_code=status.HTTP_200_OK)
async def update_position(uuid: UUID, position_data: GovernmentPositionUpdate, session: AsyncSession = Depends(get_session)):
    operations = GovernmentPositionOperations(session)
    updated_position = await operations.update(uuid, position_data.dict(exclude_unset=True))
    if not updated_position:
        raise HTTPException(status_code=404, detail="GovernmentPosition not found")
    return updated_position

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_position(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = GovernmentPositionOperations(session)
    deleted_position = await operations.delete(uuid)
    if not deleted_position:
        raise HTTPException(status_code=404, detail="GovernmentPosition not found")
    return None 