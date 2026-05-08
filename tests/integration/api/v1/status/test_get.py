import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_returns_200(client):
    response = client.get("/api/v1/status")
    assert response.status_code == 200
