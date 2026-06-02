from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.schemas.endorsement import EndorsementCreate, EndorsementResponse
from app.crud import crud_endorsement

router = APIRouter()

@router.post("/", response_model=EndorsementResponse)
async def tambah_endorsement(endorse: EndorsementCreate, db: AsyncSession = Depends(get_db)):
    return await crud_endorsement.create_endorsement(db=db, endorse=endorse)
