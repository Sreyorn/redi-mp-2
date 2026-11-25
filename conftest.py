import pytest
from fastapi.testclient import TestClient
from app.archived_task_management.main import app 

@pytest.fixture
def client():
    return TestClient(app)