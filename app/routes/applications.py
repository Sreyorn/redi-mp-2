from fastapi import APIRouter
from app.models.application import JobApplication

router = APIRouter()

@router.get('/applications')
def get_all():
    pass 

@router.post("/applications")
def create(application: JobApplication):
    pass 

