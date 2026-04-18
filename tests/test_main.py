import json
from app.main import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add_numbers():
    client = app.test_client()
    response = client.post("/add",
        data=json.dumps({"a": 5}),
        content_type="application/json"
    )

    data = json.loads(response.data)

    assert data["result"] == 999
