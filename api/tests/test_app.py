from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_reports_health_and_api_status():
    health = client.get("/api/health")
    status = client.get("/api/status")

    assert health.status_code == 200
    assert health.json()["status"] == "ok"
    assert health.json()["app"] == "fullstack-vue-fastapi-api"
    assert status.status_code == 200
    assert status.json()["status"] == "available"


def test_reports_deployment_identity():
    app_version = client.get("/api/version").json()

    assert app_version["app"] == "fullstack-vue-fastapi-api"
    assert app_version["framework"].startswith("FastAPI ")
    assert app_version["runtime"]


def test_echoes_json_without_requiring_cross_origin_access():
    response = client.post("/api/echo", json={"message": "hello"})

    assert response.status_code == 200
    assert response.json() == {"received": {"message": "hello"}}


def test_returns_api_misses_as_json():
    response = client.get("/api/missing")

    assert response.status_code == 404
    assert response.json() == {
        "error": "not_found",
        "message": "The requested API route does not exist.",
    }
