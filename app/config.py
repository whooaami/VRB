import os
from functools import lru_cache
from pydantic import EmailStr
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_ENV = os.environ.get("APP_ENV", "development")


class Settings(BaseSettings):
    DB_URI: str = ""
    ADMIN_USER: str = "admin"
    ADMIN_PASS: str = "admin"
    ADMIN_EMAIL: EmailStr = "admin@admin.com"

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=(".env",),
    )


class TestingConfig(Settings):
    """Testing configuration."""

    TESTING: bool = True

    PRESERVE_CONTEXT_ON_EXCEPTION: bool = False
    DB_URI: str = "sqlite:///database-test.db"

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=(
            ".env",
            "test.env",
        ),
        loc_by_alias=True,
    )


@lru_cache
def get_settings(name=None):
    if name is None:
        name = os.environ.get("APP_ENV", "development")

    CONF_MAP = dict(development=Settings, testing=TestingConfig)
    configuration = CONF_MAP[name]()
    configuration.APP_ENV = name
    return configuration
