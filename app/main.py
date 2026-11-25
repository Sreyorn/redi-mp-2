from fastapi import FastAPI
from app.routes.applications import router 
from app.repository.database import engine 
from app.repository import schemas

app = FastAPI()
app.include_router(router)

schemas.Base.metadata.create_all(bind=engine)