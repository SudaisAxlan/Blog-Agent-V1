from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.db.db_connection import get_session
from src.schemas.blog import CreateBlog, BlogResponse
from src.model.user import User

from src.api.security.auth import get_current_user

from src.api.services.blog import create_blog
from src.api.services.get_blogs import get_blogs


blog_router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


# ============================================
# CREATE BLOG
# ============================================

@blog_router.post("/create")
def blog_create(
    blog_data: CreateBlog,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    return create_blog(
        blog_data=blog_data,
        current_user=current_user,
        session=session
    )


# ============================================
# GET ALL BLOGS
# ============================================

@blog_router.get("/")
def blogs_get(
    # current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    return get_blogs(
        session=session
    )
