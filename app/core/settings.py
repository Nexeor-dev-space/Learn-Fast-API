from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SYNC_DATABASE_URL: str
    ASYNC_DATABASE_URL: str
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"   # point to your .env file
        extra = "ignore"    # ignore extra fields