import uuid
from pathlib import Path

import pytest

from tests.conftest import client
from tests.test_login_signup import valid_jwt

# from httpx import AsyncClient


def test_uploadfile(valid_jwt):
    boundary = uuid.uuid4().hex
    headers = {
        "Authorization": f"Bearer {valid_jwt}",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    test_file = Path("tests", "resume-sample.pdf")
    file = {
        "file": (
            "resume-sample.pdf",
            test_file.open("rb"),
            "application/pdf",
        )
    }
    response = client.post(
        "/api/services/uploadfile",
        headers=headers,
        files=file,
    )
    print(response.text)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_files(valid_jwt):
    response = client.get(
        "/api/services/get_files", headers={"Authorization": f"Bearer {valid_jwt}"}
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_jd(valid_jwt):
    response = client.get(
        "/api/services/get_jd", headers={"Authorization": f"Bearer {valid_jwt}"}
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_job_desc(valid_jwt):
    text = """
About the job
It's fun to work in a company where people truly BELIEVE in what they are doing!


We're committed to bringing passion and customer focus to the business.


Fractal Analytics is a strategic AI partner to Fortune 500 companies with a vision to power every human decision in the enterprise. Fractal is building a world where individual choices, freedom, and diversity are the greatest assets; an ecosystem where human imagination is at the heart of every decision. Where no possibility is written off, only challenged to get better.


We believe our people are the ones who truly empower imagination with intelligence. Fractal has been featured as a Great Place to Work by The Economic Times in partnership with the Great Place to Work® Institute and recognized as a 'Cool Vendor' and a 'Vendor to Watch' by Gartner.


The successful API Backend Developer will work collaboratively with our clients and teams local and global teams to deploy, automate, and operate our unique solutions for our clients.


Required Qualifications


    Experience designing and building RESTful APIs/Microservices
    Exposure to AWS platforms
    Experience with and exposure to AWS Lambda, AWS API gateway and Google Apigee (OKAPI)
    Experience with CI/CD tools such as Bamboo
    Experience building and executing unit tests using Junit (or other tools of choice)


If you like wild growth and working with happy, enthusiastic over-achievers, you'll enjoy your career with us!


Not the right fit? Let us know you are interested in a future opportunity by clicking Introduce Yourself in the top-right corner of the page or create an account to set up email alerts as new job postings become available that meet your interest!


If you like wild growth and working with happy, enthusiastic over-achievers, you'll enjoy your career with us!


Not the right fit? Let us know you're interested in a future opportunity by clicking Introduce Yourself in the top-right corner of the page or create an account to set up email alerts as new job postings become available that meet your interest!
    """
    response = client.get(
        "/api/services/job_desc?text=" + text,
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_compare(valid_jwt):
    payload = {"resume_id": 1, "JD_id": 1}
    response = client.post(
        "/api/services/compare",
        json=payload,
        headers={"Authorization": f"Bearer {valid_jwt}"},
    )
    assert response.status_code == 200
