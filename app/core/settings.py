from pydantic_settings import BaseSettings,SettingsConfigDict

class Db_Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file='.env',extra="ignore")
    ASYNC_DATABASE_URL:str

DB_Settings=Db_Settings()

class Token_Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra="ignore")
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str

Token_settings=Token_Settings()
