from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database URLs
    SYNC_DATABASE_URL: str
    ASYNC_DATABASE_URL: str

    # JWT settings
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"  # Load variables from .env
        env_file_encoding = "utf-8"

# Create a settings instance
settings = Settings()
