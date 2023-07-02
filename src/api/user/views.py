from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.api.user.schemas import UserCreate
from src.api.user.services import create_access_token, pwd_context
from src.core.config import settings
from src.db.db import db_session
from src.db.models.user.models import User

router = APIRouter()


@router.post("/signup")
async def signup(user: UserCreate, db: AsyncSession = Depends(db_session)):
    # Check if the username already exists
    existing_user = await db.execute(select(User).where(User.username == user.username))
    if existing_user.scalar():
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the password before storing
    hashed_password = pwd_context.hash(user.password)

    # Create the new user
    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    await db.commit()
    return {"message": "User created successfully"}


@router.post("/login")
async def login(user: UserCreate, db: AsyncSession = Depends(db_session)):
    # Retrieve the user from the database
    stored_user = await db.execute(select(User).where(User.username == user.username))
    stored_user = stored_user.scalar()

    if not stored_user or not pwd_context.verify(user.password, stored_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Generate JWT token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": stored_user.username, "id": stored_user.id},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
