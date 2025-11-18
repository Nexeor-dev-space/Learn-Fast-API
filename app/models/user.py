from datetime import datetime, timezone          # For created_at timestamp
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base               # Your declarative base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    fullname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships:
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship("User")

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r})"