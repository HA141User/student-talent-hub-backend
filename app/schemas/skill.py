from pydantic import BaseModel

class SkillCategoryCreate(BaseModel):
    name: str
    description: str

class SkillCategoryResponse(BaseModel):
    id: int
    name: str
    description: str
    
    class Config: 
        from_attributes = True
