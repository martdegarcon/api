from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.ministry_member.models import MinistryMember
from database.ministry_member.schemes import MinistryMemberCreate, MinistryMemberRead, MinistryMemberUpdate
from database.ministry_member.operations import MinistryMemberOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/ministry_members", tags=["ministry_members"])

@router.post("/", response_model=MinistryMemberRead, status_code=status.HTTP_201_CREATED)
async def create_member(member_data: MinistryMemberCreate, session: AsyncSession = Depends(get_session)):
    member = MinistryMember(**member_data.dict())
    operations = MinistryMemberOperations(session)
    created_member = await operations.create(member)
    return created_member

@router.get("/", response_model=List[MinistryMemberRead], status_code=status.HTTP_200_OK)
async def read_members(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = MinistryMemberOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=MinistryMemberRead, status_code=status.HTTP_200_OK)
async def read_member(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = MinistryMemberOperations(session)
    member = await operations.get(uuid)
    if not member:
        raise HTTPException(status_code=404, detail="MinistryMember not found")
    return member

@router.patch("/{uuid}", response_model=MinistryMemberRead, status_code=status.HTTP_200_OK)
async def update_member(uuid: UUID, member_data: MinistryMemberUpdate, session: AsyncSession = Depends(get_session)):
    operations = MinistryMemberOperations(session)
    updated_member = await operations.update(uuid, member_data.dict(exclude_unset=True))
    if not updated_member:
        raise HTTPException(status_code=404, detail="MinistryMember not found")
    return updated_member

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_member(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = MinistryMemberOperations(session)
    deleted_member = await operations.delete(uuid)
    if not deleted_member:
        raise HTTPException(status_code=404, detail="MinistryMember not found")
    return None 