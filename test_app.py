import pytest
from app import main  # đảm bảo tên file chính của bạn là main.py

@pytest.fixture
def client():
    with main.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the API!"}

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert response.get_json() == {"version": "1.0", "author": "Yagmur Ozden"}
