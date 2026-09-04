from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    username: str = Field(
        index=True,
        unique=True,
        max_length=50
    )

    email: str = Field(
        index=True,
        unique=True,
        max_length=255
    )

    password_hash: str

    first_name: str | None = Field(
        default=None,
        max_length=100
    )

    last_name: str | None = Field(
        default=None,
        max_length=100
    )

    

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )