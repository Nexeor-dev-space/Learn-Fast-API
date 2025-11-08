from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# ------------------------------------------------------------
# Import Base and models
# ------------------------------------------------------------
from app.db.database  import Base  # Base class
from app.db import models            # import all models so Alembic detects them

# ------------------------------------------------------------
# Import settings to get DATABASE_URL
# ------------------------------------------------------------
from app.core.config import settings

# ------------------------------------------------------------
# Alembic Config setup
# ------------------------------------------------------------
config = context.config

# Setup logging from alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for Alembic (detect models)
target_metadata = Base.metadata

# Database URL for migration (SYNC URL — not async)
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL_SYNC

# ------------------------------------------------------------
# Run migrations in 'offline' mode
# ------------------------------------------------------------
def run_migrations_offline():
    """Run migrations without a DB connection (offline mode)."""
    context.configure(
        url=SQLALCHEMY_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# ------------------------------------------------------------
# Run migrations in 'online' mode
# ------------------------------------------------------------
def run_migrations_online():
    """Run migrations with a live DB connection (online mode)."""
    connectable = engine_from_config(
        {"sqlalchemy.url": SQLALCHEMY_DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

# ------------------------------------------------------------
# Main execution
# ------------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
