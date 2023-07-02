from typing import List, Optional

from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Column, Field, Relationship, String

from src.db.models.common import TimestampModel


class File(TimestampModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="file")
    filename: str = Field(sa_column=Column(String, unique=True))
    data: str = Field(sa_column=Column(String))
    # projects: str = Field(default="", sa_column=Column(String))
    # achievements: str = Field(default="", sa_column=Column(String))
    # skills: str = Field(default="", sa_column=Column(String))
    # experience: str = Field(default="", sa_column=Column(String))

    class Config:
        arbitrary_types_allowed = True


class JobDesc(TimestampModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="jobdesc")
    data: str = Field(sa_column=Column(String))

    class Config:
        arbitrary_types_allowed = True
