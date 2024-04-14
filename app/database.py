from typing import Generator
from alchemical import Alchemical
from sqlalchemy import orm

from app.config import get_settings, Settings, APP_ENV


settings: Settings = get_settings()

if APP_ENV == "testing":
    DB_URI = "sqlite:///database-test.db"
elif APP_ENV == "development":
    DB_URI = settings.DB_URI
else:
    DB_URI = settings.DB_URI

db = Alchemical(DB_URI)


def get_db() -> Generator[orm.Session, None, None]:
    with db.Session() as session:
        yield session
