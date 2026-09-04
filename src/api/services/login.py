from fastapi import HTTPException, status
from sqlmodel import Session, select
from src.model.user import User

# from src.models.user import User
from src.schemas.user import Login

from src.api.security.password import verify_password
from src.api.security.jwt import create_access_token


def login_user(
    login_data: Login,
    session: Session
):

    user = session.exec(
        select(User).where(
            User.email == login_data.email
        )
    ).first()

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    password_correct = verify_password(
        login_data.password,
        user.password_hash
    )

    if not password_correct:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        user.id
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



# from src.model.user import User
# from src.schemas.user import CreateUser,Login
# from src.api.security.password import verify_password
# from sqlmodel import Session,select
# from fastapi import HTTPException,status




# def login_user(
#     user: Login,
#     session: Session
# ):

#     db_user = session.exec(
#         select(User).where(
#             User.email == user.email
#         )
#     ).first()

#     if not db_user:

#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid email or password"
#         )

#     password_valid = verify_password(
#         user.password,
#         db_user.password_hash
#     )

#     if not password_valid:

#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid email or password"
#         )
#     return{
#         "status":"Login Sucessfully ",
#         "user":db_user
#     }

#     # access_token = create_access_token(
#     #     db_user.id
#     # # )

#     # return {
#     #     "access_token": access_token,
#     #     "token_type": "bearer"
#     # }
