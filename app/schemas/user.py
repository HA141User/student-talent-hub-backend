from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    nim: Optional[str] = None
    name: str
    role: str = "student"

class UserResponse(BaseModel):
    id: int
    nim: Optional[str]
    name: str
    role: str
    status: str
    
    class Config: 
        from_attributes = True
