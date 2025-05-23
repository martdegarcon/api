from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.dataset_university.models import DatasetUniversity
from database.dataset_university.schemes import DatasetUniversityCreate, DatasetUniversityRead, DatasetUniversityUpdate
from database.dataset_university.operations import DatasetUniversityOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/dataset_universities", tags=["dataset_universities"])

@router.post("/", response_model=DatasetUniversityRead, status_code=status.HTTP_201_CREATED)
async def create_university(university_data: DatasetUniversityCreate, session: AsyncSession = Depends(get_session)):
    university = DatasetUniversity(**university_data.dict())
    operations = DatasetUniversityOperations(session)
    created_university = await operations.create(university)
    return created_university

@router.get("/", response_model=List[DatasetUniversityRead], status_code=status.HTTP_200_OK)
async def read_universities(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = DatasetUniversityOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=DatasetUniversityRead, status_code=status.HTTP_200_OK)
async def read_university(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = DatasetUniversityOperations(session)
    university = await operations.get(uuid)
    if not university:
        raise HTTPException(status_code=404, detail="DatasetUniversity not found")
    return university

@router.patch("/{uuid}", response_model=DatasetUniversityRead, status_code=status.HTTP_200_OK)
async def update_university(uuid: UUID, university_data: DatasetUniversityUpdate, session: AsyncSession = Depends(get_session)):
    operations = DatasetUniversityOperations(session)
    updated_university = await operations.update(uuid, university_data.dict(exclude_unset=True))
    if not updated_university:
        raise HTTPException(status_code=404, detail="DatasetUniversity not found")
    return updated_university

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_university(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = DatasetUniversityOperations(session)
    deleted_university = await operations.delete(uuid)
    if not deleted_university:
        raise HTTPException(status_code=404, detail="DatasetUniversity not found")
    return None 