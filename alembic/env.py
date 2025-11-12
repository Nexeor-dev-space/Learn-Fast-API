from logging.config import fileConfig

from sqlalchemy import pool, create_engine # We need create_engine here
from alembic import context

# Import your settings and Base model configuration
import os
import sys
# Add the project root to the path so it can find app.core and app.db
sys.path.insert(0, os.path.abspath("."))
from app.core.config import settings
from app.db.database import Base 

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# target_metadata is where we tell Alembic which SQLAlchemy models to look at.
# We set it to the Base metadata we imported from app.db.database
# C:\MyProjects\Learn-Fast-API\alembic\env.py

# ... (around line 20-30, where Base is imported)
from app.db.database import Base 

# IMPORTANT: Import all your models here so Alembic can find them!
from app.models import user # <--- MAKE SURE THIS IS PRESENT (or app.models.user)

# ... (later in the file)
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    Configures the context with just a URL.
    """
    # Use the synchronous URL for configuring the context
    url = settings.SYNC_DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    Creates an Engine and associates a connection with the context, 
    using the synchronous DB URL from our Pydantic settings.
    """
    # FIX: We use create_engine directly with the synchronous URL
    # to avoid the 'psycopg2' import error.
    connectable = create_engine(
        settings.SYNC_DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()