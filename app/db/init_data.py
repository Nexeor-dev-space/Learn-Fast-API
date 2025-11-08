# app/db/init_data.py
from sqlalchemy.orm import Session
from app.db.models import User

def init_data(db: Session):
    if db.query(User).count() == 0:
        user1 = User(username="damini", fullname="Damini Yadav", hashed_password="Damini88$#")
        user2 = User(username="admin", fullname="Admin User", hashed_password="Admin123")
        db.add_all([user1, user2])
        db.commit()
        print("✅ Initial users inserted successfully!")
    else:
        print("ℹ️ Users already exist. No new data inserted.")
