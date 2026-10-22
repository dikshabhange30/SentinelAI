



from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_events_statistics_endpoint():
    response = client.get("/events/stats/summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_events" in data
    assert "suspicious_events" in data
    assert "failed_logins" in data
    assert "successful_logins" in data
