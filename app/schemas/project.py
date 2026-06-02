from pydantic import BaseModel

class ProjectCreate(BaseModel):
    title: str
    description: str
    is_open: bool = True
    owner_id: int

class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    is_open: bool
    status: str
    owner_id: int
    
    class Config: 
        from_attributes = True

class ContributorCreate(BaseModel):
    user_id: int
    project_id: int
    role: str

class ContributorResponse(BaseModel):
    id: int
    user_id: int
    project_id: int
    role: str
    
    class Config: 
        from_attributes = True
