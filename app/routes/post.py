from fastapi import APIRouter, Depends, status, HTTPException
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

import app.model as m
from app import schema as s
from app.database import get_db

router_post = APIRouter(prefix="/posts", tags=["POSTS"])


@router_post.get("/", status_code=status.HTTP_200_OK, response_model=s.PostList)
def get_posts(db: Session = Depends(get_db)):
    posts = db.scalars(sa.select(m.Post).where(m.Post.is_deleted.is_(False))).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Posts not found"
        )

    return s.PostList(posts=posts)


@router_post.get("/{post_id}", status_code=status.HTTP_200_OK, response_model=s.PostOut)
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = db.get(m.Post, post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No such post"
        )

    return s.PostOut.model_validate(post)


@router_post.post("/", status_code=status.HTTP_201_CREATED, response_model=s.PostOut)
def create_post(post_data: s.PostIn, db: Session = Depends(get_db)):
    post = m.Post(
        title=post_data.title,
        description=post_data.description,
        author=post_data.author,
    )
    db.add(post)

    try:
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Title: {post_data.title} exists {e}",
        )

    return post


@router_post.put("/{post_id}", status_code=status.HTTP_200_OK, response_model=s.PostOut)
def update_post(post_id: int, post_data: s.PostIn, db: Session = Depends(get_db)):
    post = db.get(m.Post, post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No such post"
        )

    post.title = post_data.title
    post.description = post_data.description
    post.author = post_data.author

    try:
        db.commit()
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Title: {post_data.title} already exists",
        )

    return post


@router_post.delete(
    "/{post_id}",
    status_code=status.HTTP_200_OK,
)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(m.Post, post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No such post"
        )

    post.is_deleted = True
    db.commit()

    return "OK"
