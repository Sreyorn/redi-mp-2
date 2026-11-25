from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

# DATABASE_URL = "postgresql://sreyorn@local/jobtracker"
# sqlalchemy needs psycopg (v3) -> fix: updating the connection url to specify the driver 
DATABASE_URL = "postgresql+psycopg2://sreyorn@localhost/jobtracker"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal() 
    try: 
        yield db 
    finally:
        db.close() 
