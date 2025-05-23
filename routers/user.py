from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.user.models import User
from database.user.schemes import UserCreate, UserRead, UserUpdate
from database.user.operations import UserOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(**user_data.dict())
    operations = UserOperations(session)
    created_user = await operations.create(user)
    return created_user

@router.get("/", response_model=List[UserRead], status_code=status.HTTP_200_OK)
async def read_users(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = UserOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_user(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = UserOperations(session)
    user = await operations.get(uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{uuid}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def update_user(uuid: UUID, user_data: UserUpdate, session: AsyncSession = Depends(get_session)):
    operations = UserOperations(session)
    updated_user = await operations.update(uuid, user_data.dict(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = UserOperations(session)
    deleted_user = await operations.delete(uuid)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return None 