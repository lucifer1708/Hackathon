from typing import List, Optional

from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Column, Field, Relationship, String

from src.db.models.common import TimestampModel


class File(TimestampModel, table=True):
    """
    File model for storing file related details in database and relationship with user
    model for storing user related details in database 1and relationship with file model

    Attributes:
    ---------------
    id: int
        Id of the file
    user_id: int
        Id of the user
    user: User[]
        Relationship with user model
    filename: str
        Name of the file
    data: str
        Data of the file

    """

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="file")
    filename: str = Field(sa_column=Column(String, unique=True))
    data: str = Field(sa_column=Column(String))

    class Config:
        """
        Config class for pydantic model
        """

        arbitrary_types_allowed = True


class JobDesc(TimestampModel, table=True):
    """
    JobDesc model for storing jobdesc related details in database and relationship with
    user model for storing user related details in database 1and relationship with
    jobdesc model for storing jobdesc related details in database.

    Attributes:
    ---------------
    id: int
        Id of the jobdesc
    user_id: int
        Id of the user
    user: User[]
        Relationship with user model
    data: str
        Data of the jobdesc
    """

    id: int = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="jobdesc")
    data: str = Field(sa_column=Column(String))

    class Config:
        """
        Config class for pydantic model
        """

        arbitrary_types_allowed = True
