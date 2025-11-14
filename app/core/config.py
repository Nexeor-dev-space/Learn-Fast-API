from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # These fields match the keys in your .env file
    SYNC_DATABASE_URL: str
    ASYNC_DATABASE_URL: str
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str

    # Pydantic V2 configuration to point to .env file and ignore extra fields
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()