from pydantic import BaseModel, ConfigDict, RootModel
from datetime import datetime


class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    author: str
    publish_date: datetime
    updated_date: datetime


PostListOut = RootModel[list[PostOut]]


class PostList(BaseModel):
    posts: PostListOut


class PostIn(BaseModel):
    title: str
    description: str
    author: str
