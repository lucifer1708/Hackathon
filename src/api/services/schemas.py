from pydantic import BaseModel


class Compare(BaseModel):
    resume_id: int
    JD_id: int

    class Config:
        orm_mode = True
