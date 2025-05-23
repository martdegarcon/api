from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from database_connection import get_session
from database.political_party_member.models import PoliticalPartyMember
from database.political_party_member.schemes import PoliticalPartyMemberCreate, PoliticalPartyMemberRead, PoliticalPartyMemberUpdate
from database.political_party_member.operations import PoliticalPartyMemberOperations
from uuid import UUID
from typing import List

router = APIRouter(prefix="/political_party_members", tags=["political_party_members"])

@router.post("/", response_model=PoliticalPartyMemberRead, status_code=status.HTTP_201_CREATED)
async def create_member(member_data: PoliticalPartyMemberCreate, session: AsyncSession = Depends(get_session)):
    member = PoliticalPartyMember(**member_data.dict())
    operations = PoliticalPartyMemberOperations(session)
    created_member = await operations.create(member)
    return created_member

@router.get("/", response_model=List[PoliticalPartyMemberRead], status_code=status.HTTP_200_OK)
async def read_members(skip: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyMemberOperations(session)
    return await operations.get_all(skip=skip, limit=limit)

@router.get("/{uuid}", response_model=PoliticalPartyMemberRead, status_code=status.HTTP_200_OK)
async def read_member(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyMemberOperations(session)
    member = await operations.get(uuid)
    if not member:
        raise HTTPException(status_code=404, detail="PoliticalPartyMember not found")
    return member

@router.patch("/{uuid}", response_model=PoliticalPartyMemberRead, status_code=status.HTTP_200_OK)
async def update_member(uuid: UUID, member_data: PoliticalPartyMemberUpdate, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyMemberOperations(session)
    updated_member = await operations.update(uuid, member_data.dict(exclude_unset=True))
    if not updated_member:
        raise HTTPException(status_code=404, detail="PoliticalPartyMember not found")
    return updated_member

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_member(uuid: UUID, session: AsyncSession = Depends(get_session)):
    operations = PoliticalPartyMemberOperations(session)
    deleted_member = await operations.delete(uuid)
    if not deleted_member:
        raise HTTPException(status_code=404, detail="PoliticalPartyMember not found")
    return None 