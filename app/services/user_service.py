from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password
from app.schemas.user import UserCreate

def create_user(db: Session, user_in: UserCreate):
    hashed_pw = hash_password(user_in.password)
    db_user = User(username=user_in.username, fullname=user_in.fullname, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
