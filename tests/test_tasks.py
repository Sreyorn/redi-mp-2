from fastapi.testclient import TestClient
from app.archived_task_management.main import app
from app.archived_task_management.main import tasks
import pytest

client = TestClient(app)

# fixture: to clean up after test universally, so we don't write clean up on every test
@pytest.fixture 
def clear_tasks():
    tasks.clear();

def test_get_all_tasks():
    response = client.get("/")
    assert response.status_code == 200 


def test_add_task(clear_tasks):
    task_data={
        "title":"test task",
        "status":"todo",
        "priority":"low"
    }
    response = client.post("/task/13",json=task_data) 
    assert response.status_code == 200
    assert response.json()["title"] == "test task"



def test_get_task_by_id(clear_tasks):
    client.post("/task/1", json={
         "title":"test task",
                "status":"todo",
                "priority":"low"
    })
    res = client.get("/task/1")
    assert res.status_code== 200
    assert res.json()["id"] ==1


def test_get_task_not_found(clear_tasks):
    res = client.get("/task/1324")
    assert res.status_code == 404


def test_update_task(clear_tasks):
    task_data={
        "title":"test task",
        "status":"todo",
        "priority":"low"
    }
    edit_data={
        "title":"new title",
        "status":"todo",
        "priority":"low"
    }
    # create a task 
    client.post("/task/12", json=task_data)
    res = client.put("/task/12", json=edit_data)
    assert res.status_code == 200
    assert res.json()["title"] == "new title"


def test_delete_task(clear_tasks):
    task_data={
            "title":"test task",
            "status":"todo",
            "priority":"low"
        }
    client.post("/task/21", json=task_data)
    res = client.delete("/task/21")
    assert res.status_code == 200
    assert "21" not in res.json()

    
def test_filter_task(clear_tasks):
    some_tasks=[
        {
            "title":"task 1",
            "status":"todo",
            "priority":"low"
        },
         {
            "title":"test2",
            "status":"in_progress",
            "priority":"high"
        },
        {
            "title":"test2",
            "status":"done",
            "priority":"medium"
        },
    ]
    # create those tasks with loop
    for i,t in enumerate(some_tasks):
        client.post(f"/task/{i}", json=t)
    # filtering task with GET /tasks/{param}
    param = {"status":"todo"}
    res = client.get("/tasks/", params=param)
    for task in res.json().values():
        assert(task["status"] == "todo")
        