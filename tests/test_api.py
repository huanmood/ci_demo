import requests

def test_get_users():
    resp = requests.get("https://jsonplaceholder.typicode.com/users")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
