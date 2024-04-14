from typing import Generator
from alchemical import Alchemical
from sqlalchemy import orm

from app.config import get_settings, Settings

settings: Settings = get_settings()

DB_URI = settings.DB_URI

db = Alchemical(DB_URI)


def get_db() -> Generator[orm.Session, None, None]:
    with db.Session() as session:
        yield session
