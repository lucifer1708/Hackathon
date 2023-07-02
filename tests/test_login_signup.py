import pytest

from tests.conftest import auth_payload, client


def test_signup():
    response = client.post("/api/user/signup", json=auth_payload)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}


@pytest.fixture()
def jwt():
    response = client.post("/api/user/login", json=auth_payload)
    assert response.status_code == 200
    return response.json()["access_token"]


def test_login(jwt):
    assert jwt is not None
