from typing import Generator
from dotenv import load_dotenv
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import orm

from main import app
from app.database import get_db


load_dotenv("test.env")


@pytest.fixture
def db_session() -> Generator[orm.Session, None, None]:
    from app.database import db

    with db.Session() as session:
        db.Model.metadata.drop_all(bind=session.bind)
        db.Model.metadata.create_all(bind=session.bind)

        def override_get_db() -> Generator:
            yield session

        app.dependency_overrides[get_db] = override_get_db
        yield session

        del app.dependency_overrides[get_db]


@pytest.fixture
def client(db_session) -> Generator[TestClient, None, None]:
    """Returns a non-authorized test client for the API"""
    with TestClient(app) as c:
        yield c


@pytest.fixture
def faker_seed():
    return "some-seed"
