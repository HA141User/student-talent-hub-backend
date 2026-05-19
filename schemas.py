from pydantic import BaseModel

# --- USERS ---
class UserCreate(BaseModel):
    name: str
    role: str = "student"

class UserResponse(BaseModel):
    id: int
    name: str
    role: str
    status: str
    
    class Config: 
        from_attributes = True

# --- SKILLS (Master Data) ---
class SkillCategoryCreate(BaseModel):
    name: str
    description: str

class SkillCategoryResponse(BaseModel):
    id: int
    name: str
    description: str
    
    class Config: 
        from_attributes = True

# --- PROJECTS ---
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

# --- PROJECT CONTRIBUTORS ---
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

# --- ENDORSEMENTS ---
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