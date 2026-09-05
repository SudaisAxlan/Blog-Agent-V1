from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlmodel import Session, select

from src.db.db_connection import get_session
from src.model.user import User


# ============================================
# JWT CONFIG
# ============================================

SECRET_KEY = "your-secret-key-change-this"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ============================================
# OAUTH2
# ============================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/login"
)


# ============================================
# CREATE ACCESS TOKEN
# ============================================

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
) -> str:

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = (
            datetime.now(timezone.utc)
            + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ============================================
# GET CURRENT USER
# ============================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
) -> User:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        user_id = int(user_id)

    except (JWTError, ValueError):
        raise credentials_exception

    user = session.exec(
        select(User).where(
            User.id == user_id
        )
    ).first()

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )

    return user







# from datetime import datetime, timedelta, timezone

# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from sqlmodel import Session, select

# from src.db.db_connection import get_session
# from src.model.user import User


# # ============================================
# # JWT CONFIGURATION
# # ============================================

# SECRET_KEY = "change-this-to-a-long-random-secret-key"
# ALGORITHM = "HS256"

# ACCESS_TOKEN_EXPIRE_MINUTES = 60


# # ============================================
# # OAUTH2 SCHEME
# # ============================================

# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="/users/login"
# )


# # ============================================
# # CREATE ACCESS TOKEN
# # ============================================

# def create_access_token(
#     data: dict,
#     expires_delta: timedelta | None = None
# ) -> str:

#     to_encode = data.copy()

#     if expires_delta:
#         expire = datetime.now(timezone.utc) + expires_delta
#     else:
#         expire = (
#             datetime.now(timezone.utc)
#             + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#         )

#     to_encode.update({
#         "exp": expire
#     })

#     encoded_jwt = jwt.encode(
#         to_encode,
#         SECRET_KEY,
#         algorithm=ALGORITHM
#     )

#     return encoded_jwt


# # ============================================
# # GET CURRENT USER
# # ============================================

# def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     session: Session = Depends(get_session)
# ) -> User:

#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={
#             "WWW-Authenticate": "Bearer"
#         }
#     )

#     try:

#         # Decode JWT
#         payload = jwt.decode(
#             token,
#             SECRET_KEY,
#             algorithms=[ALGORITHM]
#         )

#         # Get user ID from token
#         user_id = payload.get("sub")

#         if user_id is None:
#             raise credentials_exception

#         user_id = int(user_id)

#     except (JWTError, ValueError):
#         raise credentials_exception

#     # Find user in database
#     user = session.exec(
#         select(User).where(
#             User.id == user_id
#         )
#     ).first()

#     if user is None:
#         raise credentials_exception

#     # Check if account is active
#     if not user.is_active:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="User account is inactive"
#         )

#     return user