from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime 

class Base(DeclarativeBase):
    pass 

class JobApplicationTable(Base):
    __tablename__ = "job_applications"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String) 
    role = Column(String) 
    location = Column(String)
    status = Column(String) 
    salary = Column(String, nullable=True) 
    notes = Column(String, nullable=True) 
    jd_raw = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now )