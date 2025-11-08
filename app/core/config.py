# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_URL_SYNC: str  # Alembic ke liye synchronous URL

    # ✅ Proper Pydantic v2 settings
    model_config = SettingsConfigDict(
        env_file=".env",              # .env file ka path
        env_file_encoding="utf-8"     # Encoding safe
    )

# ✅ Create Settings instance
settings = Settings()

print("✅ Loaded DATABASE_URL:", settings.DATABASE_URL)
