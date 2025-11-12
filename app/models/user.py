from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from app.db.database import Base # Import the Base class we just created

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    fullname: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"