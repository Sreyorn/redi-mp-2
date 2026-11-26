from fastapi import APIRouter, Depends, HTTPException
from app.models.application import JobApplication
from sqlalchemy.orm import Session 
from app.repository.database import get_db
from app.repository import schemas

router = APIRouter()

@router.get('/applications')
def get_all(db: Session = Depends(get_db)):
    return db.query(schemas.JobApplicationTable).all() 

# endpoint to get a single application
@router.get('/applications/{app_id}')
def get_one_application(app_id: int, db: Session = Depends(get_db)):
    job = db.query(schemas.JobApplicationTable).filter(schemas.JobApplicationTable.id == app_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Can't find this job")
    return job

@router.post("/applications")
def create(application: JobApplication, db: Session = Depends(get_db)):
    # convert pydantic model -> sqlalchem table obj
    # without mode='json'-> Error:   'status': <ApplicationStatus.applied: 'applied'>
    # postgresql doens't know what enum is - it expectes a plain string "applied"
    # fix: mode='json': tell Pydantic to convert enums to their values
    db_job = schemas.JobApplicationTable(**application.model_dump(mode="json"))
    # add to session
    db.add(db_job) 
    # commit to db
    db.commit() 
    # return the new record 
    db.refresh(db_job) 
    return db_job

@router.put("/applications/{app_id}")
def update_put_app(app_id: int, application: JobApplication, db:Session = Depends(get_db)):
    job = db.query(schemas.JobApplicationTable).filter(schemas.JobApplicationTable.id == app_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Can't find this job")
    # need to exclude id, and created_at when updating 
    for key, value in application.model_dump(mode='json', exclude={'id','created_at'}).items():
        setattr(job, key, value)
    db.commit()
    db.refresh(job)
    return job


@router.delete("/applications/{app_id}")
def delete_app(app_id: int, db: Session= Depends(get_db)):
    job = db.query(schemas.JobApplicationTable).filter(schemas.JobApplicationTable.id == app_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Can't find this job")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully", "id": app_id}