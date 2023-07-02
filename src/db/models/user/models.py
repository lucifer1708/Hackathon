from typing import Optional

from sqlmodel import Column, Field, Relationship, String

from src.db.models.common import TimestampModel
from src.db.models.services.models import JobDesc


class User(TimestampModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    password: str
    file: Optional["File"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="user"
    )
    jobdesc: Optional["JobDesc"] = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="user"
    )
