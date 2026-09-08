from datetime import datetime

from pydantic import BaseModel, Field



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

    image_url: str

    status: str

    author_id: int

    created_at: datetime

    updated_at: datetime



class BlogDetailResponse(BaseModel):

    id: int

    title: str

    content: str

    category: str

    image_url: str

    status: str

    author_id: int

    created_at: datetime

    updated_at: datetime


