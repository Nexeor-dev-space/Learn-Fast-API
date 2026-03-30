from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    async_database_url: str
    jwt_secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int
    test_db_url: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", case_sensitive=False, extra="allow")

settings = Settings()