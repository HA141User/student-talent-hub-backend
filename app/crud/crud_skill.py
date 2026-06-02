from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.skill import SkillCategory
from app.schemas.skill import SkillCategoryCreate

async def create_skill(db: AsyncSession, skill: SkillCategoryCreate):
    db_skill = SkillCategory(**skill.model_dump())
    db.add(db_skill)
    await db.commit()
    await db.refresh(db_skill)
    return db_skill

async def get_skills(db: AsyncSession):
    result = await db.execute(select(SkillCategory))
    return result.scalars().all()
