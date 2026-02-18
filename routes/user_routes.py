from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from db import get_db
from repositories.user_repo import UserRepo
from schemas.User_schema import UserSchema, UserResponse # Assuming UserResponse excludes password
from utils.security import get_password_hash

# You can keep these in the same router or a new one
router = APIRouter(prefix="/users", tags=["Users"])

### 1. Create User (Admin/Manual Creation)
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    
    # Check if user already exists
    if user_repo.get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password and save
    hashed_pwd = get_password_hash(user.password)
    new_user = user_repo.create_user(email=user.email, hashed_password=hashed_pwd)
    return new_user

### 2. Get All Users
@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    users = user_repo.get_all_users()
    return users

### 3. Get User by ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user = user_repo.get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {user_id} not found"
        )
    return user