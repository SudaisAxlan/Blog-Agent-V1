from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError

hash_pass = PasswordHasher()


def has_password(password: str) -> str:
    return hash_pass.hash(password)


def verify_password(
    password: str,
    password_hash: str
) -> bool:

    try:
        return hash_pass.verify(
            password_hash,
            password
        )

    except (VerifyMismatchError, VerificationError):
        return False


# def create_access_token(user_id: int) -> str:

#     expire = datetime.now(timezone.utc) + timedelta(
#         minutes=30
#     )

#     payload = {
#         "sub": str(user_id),
#         "exp": expire
#     }

#     token = jwt.encode(
#         payload,
#         SECRET_KEY,
#         algorithm=ALGORITHM
#     )

#     return token