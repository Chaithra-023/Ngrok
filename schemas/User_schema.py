from pydantic import BaseModel, EmailStr
from typing import Optional

# Base class for shared fields
class UserBase(BaseModel):
    email: EmailStr

# Schema for Input (Signup/Create)
class UserSchema(UserBase):
    password: str

# Schema for Output (What the API returns)
class UserResponse(UserBase):
    id: int
    
    class Config:
        # This is the "magic" line for SQLAlchemy compatibility
        orm_mode = True
