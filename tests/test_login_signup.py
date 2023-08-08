import pytest
from httpx import AsyncClient

from tests.conftest import app, client

auth_payload = {
    "username": "testig",
    "password": "test123",
}


def test_signup():
    response = client.post("/api/user/signup/", json=auth_payload)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}


@pytest.fixture()
async def valid_jwt():
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as ac:
        response = await ac.post("/api/user/login/", json=auth_payload)
        assert response.status_code == 200
        return response.json()["access_token"]


@pytest.mark.asyncio
async def test_login(valid_jwt):
    assert valid_jwt is not None
