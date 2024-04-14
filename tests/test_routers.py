import sqlalchemy as sa
from sqlalchemy import orm
from fastapi.testclient import TestClient
from fastapi import status

import app.model as m
from app import schema as s


def test_create_post(client: TestClient, db_session: orm.Session):
    post_data = s.PostIn(title="Test", description="TestDesc", author="TestAuthor")
    response = client.post("/api/posts/", json=post_data.model_dump())
    assert response.status_code == status.HTTP_201_CREATED
    created_post = db_session.scalar(
        sa.select(m.Post).where(m.Post.title == post_data.title)
    )
    assert created_post
    assert created_post.description == post_data.description


def test_get_posts(client: TestClient, db_session: orm.Session):
    test_post1 = m.Post(
        title="Test Post 1", description="Test Description 1", author="Test Author 1"
    )
    test_post2 = m.Post(
        title="Test Post 2", description="Test Description 2", author="Test Author 2"
    )
    db_session.add(test_post1)
    db_session.add(test_post2)
    db_session.commit()

    response = client.get("/api/posts/")
    assert response.status_code == status.HTTP_200_OK

    get_posts = db_session.scalars(
        sa.select(m.Post).where(m.Post.is_deleted.is_(False))
    ).all()
    assert get_posts == [test_post1, test_post2]


def test_get_post_by_id(client: TestClient, db_session: orm.Session):
    test_post = m.Post(
        title="Test Post", description="Test Description", author="Test Author"
    )
    db_session.add(test_post)
    db_session.commit()

    response = client.get(f"/api/posts/{test_post.id}")
    assert response.status_code == status.HTTP_200_OK

    get_post = db_session.get(m.Post, test_post.id)
    assert get_post == test_post


def test_update_post(client: TestClient, db_session: orm.Session):
    test_post = m.Post(
        title="Test Post", description="Test Description", author="Test Author"
    )
    db_session.add(test_post)
    db_session.commit()

    updated_post_data = s.PostIn(
        title="Updated Test Post",
        description="Updated Test Description",
        author="Updated Test Author",
    )
    response = client.put(
        f"/api/posts/{test_post.id}", json=updated_post_data.model_dump()
    )
    assert response.status_code == status.HTTP_200_OK

    get_post = db_session.get(m.Post, test_post.id)
    assert get_post.title == updated_post_data.title
    assert get_post.description == updated_post_data.description
    assert get_post.author == updated_post_data.author


def test_delete_post(client: TestClient, db_session: orm.Session):
    test_post = m.Post(
        title="Test Post", description="Test Description", author="Test Author"
    )
    db_session.add(test_post)
    db_session.commit()

    response = client.delete(f"/api/posts/{test_post.id}")
    assert response.status_code == status.HTTP_200_OK

    get_post = db_session.get(m.Post, test_post.id)
    assert get_post.is_deleted
