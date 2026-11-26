from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.routes.applications import router
from app.repository.database import engine, get_db
from app.repository import schemas

app = FastAPI()
app.include_router(router)

schemas.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")

@app.get("/ui")
def ui(req: Request, db: Session = Depends(get_db)):
    jobs = db.query(schemas.JobApplicationTable).all()
    return templates.TemplateResponse(request=req, name="index.html", context={"jobs": jobs})