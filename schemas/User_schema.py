from pydantic import BaseModel, EmailStr
from typing import Optional

# Base class for shared fields
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Schema for Input (Signup/Create)
class UserCreate(UserBase):
    password: str

# Schema for Output (What the API returns)
class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True
