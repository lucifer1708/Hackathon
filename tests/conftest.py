from fastapi.testclient import TestClient

from src.core.app import get_app

app = get_app()
client = TestClient(app)

auth_payload = {
    "username": "testig",
    "password": "test123",
}


