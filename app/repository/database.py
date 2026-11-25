from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

DATABASE_URL = "postgresql://sreyorn@local/jobtracker"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)