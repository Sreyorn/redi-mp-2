from pydantic import BaseModel
from datetime import datetime
class Task(BaseModel):
    id: int | None = None
    title: str
    status: str 
    description: str = ""
    priority: str 
    tags: list[str] = []
    created_at: datetime = datetime.now()

