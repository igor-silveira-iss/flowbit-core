from fastapi.testclient import TestClient

from flowbit_engine.api import app

client = TestClient(app)


def test_health_retorna_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
