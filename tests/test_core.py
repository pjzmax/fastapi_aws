from fastapi.testclient import TestClient
from fastapi import status
from api.main import app 

client = TestClient(app=app)

score = {
    "slope": 132,
    "par": 72,
    "total_score": 81
}
def test_index_returns_correct():
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World!"}

def test_create_score():
    response = client.post('/scores', json=score)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == score