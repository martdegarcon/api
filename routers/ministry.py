from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.ministry.models import Ministry
from database.ministry.schemes import MinistryCreate, MinistryRead, MinistryUpdate
from database.ministry.operations import MinistryOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/ministries", tags=["ministries"])

@router.post("/", response_model=MinistryRead, status_code=status.HTTP_201_CREATED)
async def create_ministry(ministry_data: MinistryCreate, session: AsyncSession = Depends(get_session)):
    ministry = Ministry(**ministry_data.dict())
    operations = MinistryOperations(session)
    created_ministry = await operations.create(ministry)
    return created_ministry

@router.get("/", response_model=List[MinistryRead], status_code=status.HTTP_200_OK)
async def read_ministries(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = MinistryOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=MinistryRead, status_code=status.HTTP_200_OK)
async def read_ministry(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = MinistryOperations(session)
    ministry = await operations.get(uuid)
    if not ministry:
        raise HTTPException(status_code=404, detail="Ministry not found")
    return ministry

@router.patch("/{uuid}", response_model=MinistryRead, status_code=status.HTTP_200_OK)
async def update_ministry(uuid: UUID, ministry_data: MinistryUpdate, session: AsyncSession = Depends(get_session)):
    operations = MinistryOperations(session)
    updated_ministry = await operations.update(uuid, ministry_data.dict(exclude_unset=True))
    if not updated_ministry:
        raise HTTPException(status_code=404, detail="Ministry not found")
    return updated_ministry

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_ministry(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = MinistryOperations(session)
    deleted_ministry = await operations.delete(uuid)
    if not deleted_ministry:
        raise HTTPException(status_code=404, detail="Ministry not found")
    return None 