from src.agent.graph import agent
from src.model.blog import Blog
from src.schemas.blog import CreateBlog
from sqlmodel import Session
from src.model.user import User
from sqlmodel import Session



def create_blog(
    blog_data: CreateBlog,
    current_user: User,
    session: Session
):
    result = agent.invoke(
        {
            "user_title": blog_data.title,
            "category": blog_data.category,
            "google_search": [],
            "raw_content": "",
            "formatted_content": "",
            "final_content": ""
        }
    )

    new_blog = Blog(
        title=blog_data.title,
        content=result["final_content"],
        category=blog_data.category,
        author_id=current_user.id
    )

    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)

    return new_blog