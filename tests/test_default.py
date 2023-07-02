from tests.conftest import client


def test_default():
    response = client.get("/api/health/")
    assert response.status_code == 200
    assert response.text == '"OK"'
