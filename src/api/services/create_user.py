from src.model.user import User
from src.schemas.user import CreateUser
from src.api.security.password import has_password
from sqlmodel import Session,select
from fastapi import HTTPException,status


from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.model.user import User
from src.schemas.user import CreateUser
from src.api.security.password import has_password


def create_user(
    user: CreateUser,
    session: Session
):

    existing_email = session.exec(
        select(User).where(
            User.email == user.email
        )
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered"
        )


    existing_username = session.exec(
        select(User).where(
            User.username == user.username
        )
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username is already taken"
        )


    password_hash = has_password(user.password)



    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=password_hash,
        first_name=user.first_name,
        last_name=user.last_name,
      
    )



    session.add(new_user)


    try:
        session.commit()

    except Exception:
        session.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create user"
        )

   

    session.refresh(new_user)


    return new_user