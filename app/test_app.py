import pytest
from main import app  # import từ main.py trong cùng thư mục

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the API!"}

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert response.get_json() == {"version": "1.0", "author": "Yagmur Ozden"}
