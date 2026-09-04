from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


class Blog(SQLModel, table=True):
    __tablename__ = "blogs"

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    title: str

    content: str

    category: str

    status: str = Field(
        default="draft"
    )

    author_id: int = Field(
        foreign_key="users.id",
        index=True
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )