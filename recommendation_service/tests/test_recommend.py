from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_recommend_endpoint():
    response = client.get("/recommend")
    assert response.status_code == 200
    assert response.json() == {"books": ["The Alchemist", "Sapiens"]}
