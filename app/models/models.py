from app.db.database import Base
from sqlalchemy import Column,Integer,String,DateTime,Boolean,ForeignKey
from sqlalchemy.orm import relationship
import bcrypt

class Users(Base):
    __tablename__="users"
    id =Column(Integer,primary_key=True,index=True)
    username=Column(String,nullable=False,unique=True)
    fullname=Column(String,nullable=False)
    hashed_password=Column(String,nullable=False)
    def set_password(self, password: str):
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    todos = relationship("Todo", back_populates="owner")

class Todo(Base):
    __tablename__="todo"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String)
    description=Column(String)
    completed=Column(Boolean)
    owner_id=Column(Integer,ForeignKey(Users.id),nullable=False)
    created_at=Column(DateTime)
    owner=relationship("User",back_populates="todos")