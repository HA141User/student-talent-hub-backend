from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.project import Project, ProjectContributor
from app.schemas.project import ProjectCreate, ContributorCreate

async def create_project(db: AsyncSession, project: ProjectCreate):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    await db.commit()
    await db.refresh(db_project)
    return db_project

async def get_projects(db: AsyncSession):
    result = await db.execute(select(Project))
    return result.scalars().all()

async def create_contributor(db: AsyncSession, contrib: ContributorCreate):
    db_contrib = ProjectContributor(**contrib.model_dump())
    db.add(db_contrib)
    await db.commit()
    await db.refresh(db_contrib)
    return db_contrib
