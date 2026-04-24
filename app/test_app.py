import pytest
from app import app

def test_health_endpoint():
    # create a test client and make a GET request to the /health endpoint
    with app.test_client() as client:
        response = client.get('/health')
        # Expect a 200 OK response and check the JSON content
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['service'] == 'weather-api'
