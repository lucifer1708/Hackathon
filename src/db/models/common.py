from datetime import datetime

from sqlalchemy import text
from sqlmodel import Field, SQLModel


class TimestampModel(SQLModel):
    """
    TimestampModel is a base class for all models that need to have created_at and updated_at fields.
    """

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": text("current_timestamp(0)")},
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)"),
        },
    )
