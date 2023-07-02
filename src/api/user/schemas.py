from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
