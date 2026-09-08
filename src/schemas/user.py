
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class CreateUser(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128
    )

    first_name: str | None = Field(
        default=None,
        max_length=100
    )

    last_name: str | None = Field(
        default=None,
        max_length=100
    )



class UpdateUser(BaseModel):
    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )

    email: EmailStr | None = None

    first_name: str | None = Field(
        default=None,
        max_length=100
    )

    last_name: str | None = Field(
        default=None,
        max_length=100
    )


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    first_name: str | None
    last_name: str | None

    is_active: bool
    is_verified: bool

    created_at: datetime
    updated_at: datetime



class Login(BaseModel):

    email: EmailStr
    
    password: str = Field(
            min_length=6,
            max_length=128
        )