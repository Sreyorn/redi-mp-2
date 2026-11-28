from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class ApplicationStatus(Enum):
    applied = "applied"
    rejected = "rejected"
    interviewed = "interviewed"
    offered = "offered"

class JobApplication(BaseModel):
    id: int | None = None
    company: str 
    role: str
    location: str
    status: ApplicationStatus
    salary: str | None = None
    notes: str | None = None 
    jd_raw: str | None = None
    created_at: datetime = datetime.now() 

