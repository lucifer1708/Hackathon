from pydantic import BaseModel


class Compare(BaseModel):
    """
    Compare schema for SWOT analysis of resume
    Attributes:
    ----------------
    resume_id: int
        The id of the resume to be compared.
    JD_id: int
        The id of the JD to be compared.
    """

    resume_id: int
    JD_id: int

    class Config:
        orm_mode = True
