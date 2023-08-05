from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.config import settings

# Create the async engine
async_engine = create_async_engine(settings.DB_URL, echo=settings.DB_ECHO, future=True)

Base = declarative_base()


async def db_session() -> AsyncGenerator:
    """
    Creates a new async session for each request and closes it after the request is finished.
    """
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with async_session() as session:
        yield session
