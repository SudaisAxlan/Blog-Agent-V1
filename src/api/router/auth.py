from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from src.model.user import User
# from src.schema.user import LoginUser
from src.api.security.jwt import create_access_token
from src.api.security.password import verify_password

from src.schemas.user import CreateUser,Login
from src.db.db_connection import get_session



router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(
    user: Login,
    session: Session = Depends(get_session)
):

    db_user = session.exec(
        select(User).where(
            User.email == user.email
        )
    ).first()

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        db_user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        db_user.id
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }