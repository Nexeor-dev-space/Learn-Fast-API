<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from app.core.database import Base  # make sure this Base is the same used in Alembic
=======
# app/models.py
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

Base = declarative_base()  # <- this is the Base Alembic needs
>>>>>>> main-daminiyadav23

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
<<<<<<< HEAD
    username = Column(String, unique=True, nullable=False)
    fullname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
=======
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
>>>>>>> main-daminiyadav23
