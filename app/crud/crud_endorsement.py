from sqlalchemy.ext.asyncio import AsyncSession
from app.models.endorsement import Endorsement
from app.schemas.endorsement import EndorsementCreate

async def create_endorsement(db: AsyncSession, endorse: EndorsementCreate):
    db_endorse = Endorsement(**endorse.model_dump())
    db.add(db_endorse)
    await db.commit()
    await db.refresh(db_endorse)
    return db_endorse
