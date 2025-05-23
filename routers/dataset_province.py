from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.dataset_province.models import DatasetProvince
from database.dataset_province.schemes import DatasetProvinceCreate, DatasetProvinceRead, DatasetProvinceUpdate
from database.dataset_province.operations import DatasetProvinceOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/dataset_provinces", tags=["dataset_provinces"])

@router.post("/", response_model=DatasetProvinceRead, status_code=status.HTTP_201_CREATED)
async def create_province(province_data: DatasetProvinceCreate, session: AsyncSession = Depends(get_session)):
    province = DatasetProvince(**province_data.dict())
    operations = DatasetProvinceOperations(session)
    created_province = await operations.create(province)
    return created_province

@router.get("/", response_model=List[DatasetProvinceRead], status_code=status.HTTP_200_OK)
async def read_provinces(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = DatasetProvinceOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=DatasetProvinceRead, status_code=status.HTTP_200_OK)
async def read_province(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = DatasetProvinceOperations(session)
    province = await operations.get(uuid)
    if not province:
        raise HTTPException(status_code=404, detail="DatasetProvince not found")
    return province

@router.patch("/{uuid}", response_model=DatasetProvinceRead, status_code=status.HTTP_200_OK)
async def update_province(uuid: UUID, province_data: DatasetProvinceUpdate, session: AsyncSession = Depends(get_session)):
    operations = DatasetProvinceOperations(session)
    updated_province = await operations.update(uuid, province_data.dict(exclude_unset=True))
    if not updated_province:
        raise HTTPException(status_code=404, detail="DatasetProvince not found")
    return updated_province

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_province(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = DatasetProvinceOperations(session)
    deleted_province = await operations.delete(uuid)
    if not deleted_province:
        raise HTTPException(status_code=404, detail="DatasetProvince not found")
    return None 