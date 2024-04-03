from fastapi.testclient import TestClient
from fastapi import status
from main import app

test_client = TestClient(app)


def test_return_health_check():
    response = test_client.get('/healthy')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'Healthy'}