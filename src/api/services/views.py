import json

import openai
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlmodel import and_, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.api.services.schemas import Compare
from src.api.user.services import get_current_user
from src.core.config import settings
from src.db.db import db_session
from src.db.models.services.models import File as FileModel
from src.db.models.services.models import JobDesc
from src.deps.services import (compare_completion_from_messages, compare_system_message,
                               get_completion_from_messages, jd_system_message,
                               system_message)
from src.deps.utils import read_pdf

router = APIRouter()
openai.api_key = f"{settings.OPENAI_APIKEY}"


@router.post("/uploadfile")
async def uploadfile(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(db_session),
    current_user: dict = Depends(get_current_user),
):
    """
    Upload a file to the server and save it in the database.
    Attributes:
    --------------
    file: file to upload
    db: database session
    current_user: current user

    Returns:
    --------------
    message: success message
    """
    with open(file.filename, "wb") as f:
        f.write(await file.read())
    extracted_text = read_pdf(file.filename)
    messages = [
        {"role": "system", "content": system_message},
        {
            "role": "assistant",
            "content": f"""Relevant resume content: \n
       {extracted_text}""",
        },
    ]
    text = get_completion_from_messages(messages)
    content = FileModel(
        user_id=current_user["id"],
        filename=file.filename,
        data=str(text),
    )
    db.add(content)
    await db.commit()
    return {"message": "File uploaded successfully"}


@router.get("/get_files")
async def get_files(
    db: AsyncSession = Depends(db_session),
    current_user: dict = Depends(get_current_user),
):
    """
    Get all files from the database.

    Attributes:
    --------------
    db: database session
    current_user: current user

    Returns:
    --------------
    files: list of files
    """
    files = await db.execute(
        select(FileModel).where(FileModel.user_id == current_user["id"])
    )
    return files.scalars().all()


@router.get("/get_jd")
async def get_jd(
    db: AsyncSession = Depends(db_session),
    current_user: dict = Depends(get_current_user),
):
    """
    Get all job descriptions from the database.

    Attributes:
    --------------
    db: database session
    current_user: current user

    Returns:
    --------------
    jobdesc: list of job descriptions
    """
    jobdesc = await db.execute(
        select(JobDesc).where(JobDesc.user_id == current_user["id"])
    )
    return jobdesc.scalars().all()


@router.get("/jobdesc")
async def Job_Desc(
    text: str,
    db: AsyncSession = Depends(db_session),
    current_user: dict = Depends(get_current_user),
):
    """
    Get all job descriptions from the database.

    Attributes:
    --------------
    text: text to be processed
    db: database session
    current_user: current user

    Returns:
    --------------
    jobdesc: list of job descriptions
    """
    messages = [
        {"role": "system", "content": jd_system_message},
        {
            "role": "assistant",
            "content": f"""Relevant Job description information: \n
       {text}""",
        },
    ]
    text = get_completion_from_messages(messages)
    text = json.loads(text)
    content = JobDesc(
        user_id=current_user["id"],
        data=str(text),
    )
    db.add(content)
    await db.commit()
    return text


@router.post("/compare")
async def compare(
    compare: Compare,
    db: AsyncSession = Depends(db_session),
    current_user: dict = Depends(get_current_user),
):
    """
    Compare a resume with a job description.

    Attributes:
    --------------
    compare: resume and job description to compare
    db: database session
    current_user: current user

    Returns:
    --------------
    results : comparison result
    """
    resume_id = compare.resume_id
    JD_id = compare.JD_id

    # Check if the current user owns the specified data_id
    resume = await db.execute(
        select(FileModel).where(
            and_(FileModel.id == resume_id, FileModel.user_id == current_user["id"])
        )
    )
    owned_resume = resume.scalar()

    if not owned_resume:
        raise HTTPException(
            status_code=403, detail="You do not have access to the specified data."
        )

    jd = await db.execute(
        select(JobDesc).where(
            and_(JobDesc.id == JD_id, JobDesc.user_id == current_user["id"])
        )
    )
    retrieved_jd = jd.scalar()

    if not retrieved_jd:
        raise HTTPException(status_code=404, detail="Data with data1_id not found.")
    messages = [
        {"role": "system", "content": compare_system_message},
        {"role": "user", "content": owned_resume.data},
        {
            "role": "assistant",
            "content": f"""Relevant Job description information: \n
  {retrieved_jd.data}""",
        },
    ]
    text = compare_completion_from_messages(messages)
    text = json.loads(text)
    return text
