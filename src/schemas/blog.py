from pydantic import BaseModel, Field


class CreateBlog(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=200
    )

    content: str = Field(
        min_length=10
    )

    category: str = Field(
        min_length=2,
        max_length=100
    )