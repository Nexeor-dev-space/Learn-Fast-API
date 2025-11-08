# app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings  # yahan se DATABASE_URL aayegi

# ---------------------------------------------------
# 1️⃣ Database Engine
# ---------------------------------------------------
engine = create_engine(settings.DATABASE_URL)

# ---------------------------------------------------
# 2️⃣ SessionLocal: used to talk to the DB
# ---------------------------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ---------------------------------------------------
# 3️⃣ Dependency function for FastAPI routes
# ---------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
