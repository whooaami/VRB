from functools import lru_cache
from pydantic import EmailStr
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    DB_URI: str = ""
    ADMIN_USER: str = "admin"
    ADMIN_PASS: str = "admin"
    ADMIN_EMAIL: EmailStr = "admin@admin.com"

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=(".env",),
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
