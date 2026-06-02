from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.crud import crud_user

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def tambah_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud_user.create_user(db=db, user=user)

@router.get("/", response_model=List[UserResponse])
async def ambil_semua_user(db: AsyncSession = Depends(get_db)):
    return await crud_user.get_users(db=db)
