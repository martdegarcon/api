from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.user_group.models import UserGroup
from database.user_group.schemes import UserGroupCreate, UserGroupRead, UserGroupUpdate
from database.user_group.operations import UserGroupOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/user_groups", tags=["user_groups"])

@router.post("/", response_model=UserGroupRead, status_code=status.HTTP_201_CREATED)
async def create_user_group(group_data: UserGroupCreate, session: AsyncSession = Depends(get_session)):
    group = UserGroup(**group_data.dict())
    operations = UserGroupOperations(session)
    created_group = await operations.create(group)
    return created_group

@router.get("/", response_model=List[UserGroupRead], status_code=status.HTTP_200_OK)
async def read_user_groups(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = UserGroupOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=UserGroupRead, status_code=status.HTTP_200_OK)
async def read_user_group(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = UserGroupOperations(session)
    group = await operations.get(uuid)
    if not group:
        raise HTTPException(status_code=404, detail="UserGroup not found")
    return group

@router.patch("/{uuid}", response_model=UserGroupRead, status_code=status.HTTP_200_OK)
async def update_user_group(uuid: UUID, group_data: UserGroupUpdate, session: AsyncSession = Depends(get_session)):
    operations = UserGroupOperations(session)
    updated_group = await operations.update(uuid, group_data.dict(exclude_unset=True))
    if not updated_group:
        raise HTTPException(status_code=404, detail="UserGroup not found")
    return updated_group

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_group(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = UserGroupOperations(session)
    deleted_group = await operations.delete(uuid)
    if not deleted_group:
        raise HTTPException(status_code=404, detail="UserGroup not found")
    return None 