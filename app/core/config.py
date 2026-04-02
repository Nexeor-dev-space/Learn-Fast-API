from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    sync_database_url: str
    async_database_url: str

    postgres_user: str
    postgres_password: str
    postgres_db: str

    test_db_url: str

    jwt_secret_key: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int
    jwt_algorithm: str    
    model_config = SettingsConfigDict(env_file=".env", env_prefix="", case_sensitive=False, extra="allow")

settings = Settings()