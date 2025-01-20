DEBUG = True  # Set to True for development, False for production

#Db config
DB_CONNECTION = ''


# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str = "sqlite:///./test.db"
    secret_key: str = "mysecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"  # Loads environment variables from an .env file

settings = Settings()
