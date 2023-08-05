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
    """
    Create a new user in the database and return a message if successful or raise an exception if the username already exists in the database.

    Arguments:
    ---------------
    user: UserCreate
        The user to be created in the database.
    db: AsyncSession = Depends(db_session)
        The database session.

    Returns:
    --------------
    dict: A dictionary containing a message if the user was created successfully.
    """
    existing_user = await db.execute(select(User).where(User.username == user.username))
    if existing_user.scalar():
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    await db.commit()
    return {"message": "User created successfully"}


@router.post("/login")
async def login(user: UserCreate, db: AsyncSession = Depends(db_session)):
    """
    Check if the user exists in the database and if the password is correct. If so, return an access token.

    Arguments:
    ---------------
    user: UserCreate
        The user created in the database.
    db: AsyncSession = Depends(db_session)
        The database session.

    Returns:
    --------------
    dict: A dictionary containing an access token if the user exists in the database and the password is correct.
    """
    stored_user = await db.execute(select(User).where(User.username == user.username))
    stored_user = stored_user.scalar()

    if not stored_user or not pwd_context.verify(user.password, stored_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": stored_user.username, "id": stored_user.id},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
