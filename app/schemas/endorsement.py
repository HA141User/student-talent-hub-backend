from pydantic import BaseModel

class EndorsementCreate(BaseModel):
    from_user_id: int
    to_user_id: int
    skill_id: int
    project_id: int
    message: str

class EndorsementResponse(BaseModel):
    id: int
    from_user_id: int
    to_user_id: int
    skill_id: int
    project_id: int
    message: str
    
    class Config:
        from_attributes = True
