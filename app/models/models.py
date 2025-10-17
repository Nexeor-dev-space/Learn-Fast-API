from app.db.database import Base
from sqlalchemy import Column,Integer,String
import bcrypt

class Users(Base):
    __tablename__="users"
    id =Column(Integer,primary_key=True,index=True)
    username=Column(String,nullable=False,unique=True)
    fullname=Column(String,nullable=False)
    password=Column(String,nullable=False)
    def set_password(self, password: str):
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')