from typing import Optional

from sqlmodel import Field, Relationship

from src.db.models.common import TimestampModel
from src.db.models.services.models import File, JobDesc


class User(TimestampModel, table=True):
    """
    User model for storing user related details in database.

    Attributes:
    ------------
    id: int
        Primary key for the user table.
    username: str
        Username of the user.
    password: str
        Password of the user.
    file: File[]
        File object associated with the user.
    jobdesc: JobDesc[]
        JobDesc object associated with the user.
    """

    id: int = Field(default=None, primary_key=True)
    username: str
    password: str
    file: Optional["File"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="user"
    )
    jobdesc: Optional["JobDesc"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="user"
    )
