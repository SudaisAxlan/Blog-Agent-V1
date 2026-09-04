from sqlmodel import Session, select

from src.model.blog import Blog


def get_blogs(
    session: Session
):
    blogs = session.exec(select(Blog).order_by(Blog.created_at.desc())).all()

    return blogs