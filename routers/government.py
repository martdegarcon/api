from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.government.models import Government
from database.government.schemes import GovernmentCreate, GovernmentRead, GovernmentUpdate
from database.government.operations import GovernmentOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/governments", tags=["governments"])

@router.post("/", response_model=GovernmentRead, status_code=status.HTTP_201_CREATED)
async def create_government(government_data: GovernmentCreate, session: AsyncSession = Depends(get_session)):
    government = Government(**government_data.dict())
    operations = GovernmentOperations(session)
    created_government = await operations.create(government)
    return created_government

@router.get("/", response_model=List[GovernmentRead], status_code=status.HTTP_200_OK)
async def read_governments(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = GovernmentOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=GovernmentRead, status_code=status.HTTP_200_OK)
async def read_government(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = GovernmentOperations(session)
    government = await operations.get(uuid)
    if not government:
        raise HTTPException(status_code=404, detail="Government not found")
    return government

@router.patch("/{uuid}", response_model=GovernmentRead, status_code=status.HTTP_200_OK)
async def update_government(uuid: UUID, government_data: GovernmentUpdate, session: AsyncSession = Depends(get_session)):
    operations = GovernmentOperations(session)
    updated_government = await operations.update(uuid, government_data.dict(exclude_unset=True))
    if not updated_government:
        raise HTTPException(status_code=404, detail="Government not found")
    return updated_government

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_government(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = GovernmentOperations(session)
    deleted_government = await operations.delete(uuid)
    if not deleted_government:
        raise HTTPException(status_code=404, detail="Government not found")
    return None 