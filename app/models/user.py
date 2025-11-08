from sqlalchemy import Column, Integer, String
<<<<<<< HEAD
from app.db.base_class import Base
=======
from sqlalchemy.orm import declarative_base

Base = declarative_base()
>>>>>>> main-daminiyadav23

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
<<<<<<< HEAD
    username = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
=======
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
>>>>>>> main-daminiyadav23
