from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API. Check /docs for usage"}

def test_predict_tags():
    response = client.post("/predict", json={"text": "How to use Python for data analysis?"})
    assert response.status_code == 200
    assert "tags" in response.json()
