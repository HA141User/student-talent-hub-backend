from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from typing import List

from app.api.dependencies import get_db, get_current_user
from app.schemas.user import UserCreate, UserResponse, Token
from app.crud import crud_user
from app.core.security import verify_password, create_access_token
from app.models.user import User

router = APIRouter()

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED) # 1. Ubah response_model menjadi Token
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    if user.nim:
        db_user_nim = await crud_user.get_user_by_nim(db, nim=user.nim)
        if db_user_nim:
            raise HTTPException(status_code=400, detail="NIM already registered")
            
    # 2. Simpan user baru ke database dan tampung hasilnya ke variabel
    new_user = await crud_user.create_user(db=db, user=user)
    
    # 3. Generate token JWT secara otomatis menggunakan email dari user baru
    access_token = create_access_token(data={"sub": new_user.email})
    
    # 4. Kembalikan payload token sesuai dengan schema Token
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    # OAuth2PasswordRequestForm uses 'username' field for the email by default
    user = await crud_user.get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=List[UserResponse])
async def ambil_semua_user(db: AsyncSession = Depends(get_db)):
    return await crud_user.get_users(db=db)
