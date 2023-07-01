from src.db.models.common import TimestampModel, UUIDModel


class User(TimestampModel, UUIDModel, table=True):
    __tablename__ = "users"

    username: str
    password: str

    def __repr__(self):
        return f"<User (id: {self.id})>"
