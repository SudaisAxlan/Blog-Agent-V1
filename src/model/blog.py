from datetime import datetime, timezone

from sqlmodel import SQLModel, Field


DEFAULT_BLOG_IMAGE = (
    "https://res.cloudinary.com/vebwwyza/image/upload/"
    "v1787654759/gpg2hwbiespnrovxtcai.jpg"
)


class Blog(SQLModel, table=True):
    __tablename__ = "blogs"

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    title: str

    content: str

    category: str

    image_url: str = Field(
        default=DEFAULT_BLOG_IMAGE,
        max_length=1000
    )

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



    
# from datetime import datetime, timezone

# from sqlmodel import SQLModel, Field


# class Blog(SQLModel, table=True):
#     __tablename__ = "blogs"

#     id: int | None = Field(
#         default=None,
#         primary_key=True
#     )

#     title: str

#     content: str

#     category: str

#     status: str = Field(
#         default="draft"
#     )

#     author_id: int = Field(
#         foreign_key="users.id",
#         index=True
#     )

#     created_at: datetime = Field(
#         default_factory=lambda: datetime.now(timezone.utc)
#     )

#     updated_at: datetime = Field(
#         default_factory=lambda: datetime.now(timezone.utc)
#     )