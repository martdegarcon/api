from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.dataset_gender.models import DatasetGender
from database.dataset_gender.schemes import DatasetGenderCreate, DatasetGenderRead, DatasetGenderUpdate
from database.dataset_gender.operations import DatasetGenderOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/dataset_genders", tags=["dataset_genders"])

@router.post("/", response_model=DatasetGenderRead, status_code=status.HTTP_201_CREATED)
async def create_gender(gender_data: DatasetGenderCreate, session: AsyncSession = Depends(get_session)):
    gender = DatasetGender(**gender_data.dict())
    operations = DatasetGenderOperations(session)
    created_gender = await operations.create(gender)
    return created_gender

@router.get("/", response_model=List[DatasetGenderRead], status_code=status.HTTP_200_OK)
async def read_genders(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = DatasetGenderOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=DatasetGenderRead, status_code=status.HTTP_200_OK)
async def read_gender(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = DatasetGenderOperations(session)
    gender = await operations.get(uuid)
    if not gender:
        raise HTTPException(status_code=404, detail="DatasetGender not found")
    return gender

@router.patch("/{uuid}", response_model=DatasetGenderRead, status_code=status.HTTP_200_OK)
async def update_gender(uuid: UUID, gender_data: DatasetGenderUpdate, session: AsyncSession = Depends(get_session)):
    operations = DatasetGenderOperations(session)
    updated_gender = await operations.update(uuid, gender_data.dict(exclude_unset=True))
    if not updated_gender:
        raise HTTPException(status_code=404, detail="DatasetGender not found")
    return updated_gender

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_gender(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = DatasetGenderOperations(session)
    deleted_gender = await operations.delete(uuid)
    if not deleted_gender:
        raise HTTPException(status_code=404, detail="DatasetGender not found")
    return None 