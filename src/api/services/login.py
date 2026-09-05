from fastapi import HTTPException, status
from sqlmodel import Session, select

from src.model.user import User
from src.schemas.user import Login
from src.api.security.password import verify_password
from src.api.security.jwt import create_access_token


def login_user(
    login_data: Login,
    session: Session
):
    # ============================================
    # FIND USER BY EMAIL
    # ============================================

    user = session.exec(
        select(User).where(
            User.email == login_data.email
        )
    ).first()

    # ============================================
    # CHECK USER
    # ============================================

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    # ============================================
    # VERIFY PASSWORD
    # ============================================

    password_valid = verify_password(
        login_data.password,
        user.password_hash
    )

    if not password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    # ============================================
    # CHECK ACCOUNT STATUS
    # ============================================

    

    # ============================================
    # CREATE JWT ACCESS TOKEN
    # ============================================

    access_token = create_access_token(
        data={
            "sub": str(user.id)
        }
    )

    # ============================================
    # RETURN TOKEN
    # ============================================

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }