from pydantic import BaseModel


class UserSchema(BaseModel):
    """
    UserSchema representing details of login form for authentication.

    Attributes:
    ----------------
    username: str
        The username of the user.
    password: str
        The password of the user.
    """

    username: str
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    """
    UserCreate representing details of signup form for authentication.

    Attributes:
    ----------------
    username: str
        The username of the user.
    password: str
        The password of the user.
    """

    username: str
    password: str

    class Config:
        orm_mode = True
