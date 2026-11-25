from fastapi import APIRouter, Depends
from app.models.application import JobApplication
from sqlalchemy.orm import Session 
from app.repository.database import get_db
from app.repository import schemas

router = APIRouter()

@router.get('/applications')
def get_all(db: Session = Depends(get_db)):
    return db.query(schemas.JobApplicationTable).all() 


@router.post("/applications")
def create(application: JobApplication, db: Session = Depends(get_db)):
    # convert pydantic model -> sqlalchem table obj
    # without mode='json'-> Error:   'status': <ApplicationStatus.applied: 'applied'>
    # postgresql doens't know what enum is - it expectes a plain string "applied"
    # fix: mode='json': tell Pydantic to convert enums to their values
    db_item = schemas.JobApplicationTable(**application.model_dump(mode="json"))
    # add to session
    db.add(db_item) 
    # commit to db
    db.commit() 
    # return the new record 
    db.refresh(db_item) 
    return db_item


