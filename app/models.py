from sqlalchemy import Column, Integer, String
from app.db.base_class import Base  # your declarative base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
