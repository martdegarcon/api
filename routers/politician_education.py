from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.politician_education.models import PoliticianEducation
from database.politician_education.schemes import PoliticianEducationCreate, PoliticianEducationRead, PoliticianEducationUpdate
from database.politician_education.operations import PoliticianEducationOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/politician_educations", tags=["politician_educations"])

@router.post("/", response_model=PoliticianEducationRead, status_code=status.HTTP_201_CREATED)
async def create_education(education_data: PoliticianEducationCreate, session: AsyncSession = Depends(get_session)):
    education = PoliticianEducation(**education_data.dict())
    operations = PoliticianEducationOperations(session)
    created_education = await operations.create(education)
    return created_education

@router.get("/", response_model=List[PoliticianEducationRead], status_code=status.HTTP_200_OK)
async def read_educations(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = PoliticianEducationOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=PoliticianEducationRead, status_code=status.HTTP_200_OK)
async def read_education(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticianEducationOperations(session)
    education = await operations.get(uuid)
    if not education:
        raise HTTPException(status_code=404, detail="PoliticianEducation not found")
    return education

@router.patch("/{uuid}", response_model=PoliticianEducationRead, status_code=status.HTTP_200_OK)
async def update_education(uuid: UUID, education_data: PoliticianEducationUpdate, session: AsyncSession = Depends(get_session)):
    operations = PoliticianEducationOperations(session)
    updated_education = await operations.update(uuid, education_data.dict(exclude_unset=True))
    if not updated_education:
        raise HTTPException(status_code=404, detail="PoliticianEducation not found")
    return updated_education

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_education(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticianEducationOperations(session)
    deleted_education = await operations.delete(uuid)
    if not deleted_education:
        raise HTTPException(status_code=404, detail="PoliticianEducation not found")
    return None 