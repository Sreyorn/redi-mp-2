from fastapi import FastAPI
from app.routes.applications import router 

app = FastAPI()
app.include_router(router)
