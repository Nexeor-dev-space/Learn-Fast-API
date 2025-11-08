from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
from app.db.database import Base  # 👈 zaroori import

# ✅ Database URL (sync version)
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL_SYNC

# ✅ Engine create karo
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ✅ Session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
from sqlalchemy.orm import declarative_base

# --------------------------------------------------------
# 👇 Base class — sabhi models isi se inherit karenge
# --------------------------------------------------------
Base = declarative_base()


# ✅ Base class (agar Base import nahi hota to uncomment karo niche line)
# Base = declarative_base()

# ✅ Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
