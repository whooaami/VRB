import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime

from app.database import db


class Post(db.Model):
    __tablename__ = "posts"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(
        sa.String(256), nullable=False, unique=True
    )
    description: orm.Mapped[str] = orm.mapped_column(sa.String(256))
    author: orm.Mapped[str] = orm.mapped_column(sa.String(256), nullable=False)
    publish_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=datetime.now
    )
    updated_date: orm.Mapped[datetime] = orm.mapped_column(
        sa.DateTime, default=datetime.now, onupdate=datetime.now
    )

    is_deleted: orm.Mapped[bool] = orm.mapped_column(sa.Boolean, default=False)

    def __str__(self) -> str:
        return f"<Post {self.title}> Description: {self.description}"
