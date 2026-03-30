from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    async_database_url: str
    jwt_secret_key: str
    jwt_algorithm: str 
    access_token_expire_minutes: int 
    refresh_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()