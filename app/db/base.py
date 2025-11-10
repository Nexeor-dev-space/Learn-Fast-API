# app/db/base.py

# ----------------------------------------------------
# Ye file alembic ko saare models detect karne me help karti hai
# ----------------------------------------------------

from app.db.database import Base  # Base = declarative_base()
from app.db.models import user  # 👈 yaha sabhi models import karo (like user, post, etc.)

# Agar tumhare paas aur models hain, unhe bhi import karo, jaise:
# from app.db.models import post, comment, etc.

from sqlalchemy.orm import declarative_base

Base = declarative_base()
