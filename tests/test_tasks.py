from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_tasks():
    response = client.get("/")
    assert response.status_code == 200 


def test_add_task():
    response = client.post("/task/13",json={
        "title":"test task",
        "status":"todo",
        "priority":"low"
    }) 
    assert response.status_code == 200
    assert response.json()["title"] == "test task"


def test_get_task_by_id():
    client.post("/task/1", json={
         "title":"test task",
                "status":"todo",
                "priority":"low"
    })
    res = client.get("/task/1")
    assert res.status_code== 200
    assert res.json()["id"] ==1


def test_get_task_not_found():
    res = client.get("/task/1324")
    assert res.status_code == 404