from sqlalchemy import Column, Integer, String
from app.db.database import Base  # import your Base from database.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
