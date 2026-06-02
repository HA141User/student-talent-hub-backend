from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.dependencies import get_db
from app.schemas.project import ProjectCreate, ProjectResponse, ContributorCreate, ContributorResponse
from app.crud import crud_project

router = APIRouter()

@router.post("/", response_model=ProjectResponse)
async def tambah_project(project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    return await crud_project.create_project(db=db, project=project)

@router.get("/", response_model=List[ProjectResponse])
async def ambil_semua_project(db: AsyncSession = Depends(get_db)):
    return await crud_project.get_projects(db=db)

@router.post("/contributors", response_model=ContributorResponse)
async def tambah_kolaborator(contrib: ContributorCreate, db: AsyncSession = Depends(get_db)):
    return await crud_project.create_contributor(db=db, contrib=contrib)
