from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.dependencies import get_db
from app.schemas.skill import SkillCategoryCreate, SkillCategoryResponse
from app.crud import crud_skill

router = APIRouter()

@router.post("/", response_model=SkillCategoryResponse)
async def tambah_skill(skill: SkillCategoryCreate, db: AsyncSession = Depends(get_db)):
    return await crud_skill.create_skill(db=db, skill=skill)

@router.get("/", response_model=List[SkillCategoryResponse])
async def ambil_semua_skill(db: AsyncSession = Depends(get_db)):
    return await crud_skill.get_skills(db=db)
