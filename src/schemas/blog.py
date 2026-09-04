from pydantic import BaseModel, Field
from datetime import datetime


class CreateBlog(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=200
    )



    category: str = Field(
        min_length=2,
        max_length=100
    )




class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    category: str
    status: str
    author_id: int
    created_at: datetime
    updated_at: datetime



class BlogDetailResponse(BaseModel):
    id: int
    title: str

    raw_content: str | None = None
    formatted_content: str | None = None
    final_content: str | None = None

    status: str

    created_at: datetime
    updated_at: datetime