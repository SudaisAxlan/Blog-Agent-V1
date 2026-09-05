from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.db.db_connection import get_session

from src.schemas.user import CreateUser, Login
from src.model.user import User

from src.api.services.create_user import create_user
from src.api.services.login import login_user


from src.api.security.auth import get_current_user

# from src.models.user import User


user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# --------------------------------
# CREATE USER
# --------------------------------

@user_router.post("/create")
def user_create(
    user: CreateUser,
    session: Session = Depends(get_session)
):

    return create_user(
        user=user,
        session=session
    )


# --------------------------------
# LOGIN
# --------------------------------

@user_router.post("/login")
def user_login(
    login_data: Login,
    session: Session = Depends(get_session)
):

    return login_user(
        login_data=login_data,
        session=session
    )


# --------------------------------
# CURRENT USER
# --------------------------------

@user_router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    return current_user

# from fastapi import APIRouter, Depends
# from sqlmodel import Session

# from src.schemas.user import CreateUser,Login

# from src.schemas.user import CreateUser
# from src.db.db_connection import get_session
# from src.api.security.password import has_password
# from src.api.services.login import login_user
# from src.api.services.create_user import create_user

# # from src.schama.user import CreateUser,Login
# # from src.services.user import create_user,login_user


# user_router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )


# @user_router.post("/create")
# def user_create(
#     user: CreateUser,
#     session: Session = Depends(get_session)
# ):
    

#     return create_user(user=user,session=session)



# @user_router.post("/login")
# def user_login(
#     login_data: Login,
#     session: Session = Depends(get_session)
# ):

#     return login_user(
#         login_data=login_data,
#         session=session
#     )