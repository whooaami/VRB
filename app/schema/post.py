from pydantic import (
    BaseModel,
    ConfigDict,
)
from datetime import datetime


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    author: str
    publish_date: datetime
    updated_date: datetime


class PostList(BaseModel):
    posts: list[PostOut]


class PostIn(BaseModel):
    title: str
    description: str
    author: str
