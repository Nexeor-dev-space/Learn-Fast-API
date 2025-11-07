from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Password: Damini88$#
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Damini88%%24%%23@localhost:5432/fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
