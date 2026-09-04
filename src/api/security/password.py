from argon2 import PasswordHasher
from datetime import datetime, timedelta, timezone

# import jwt
# from argon2 import PasswordHasher
# from argon2.exceptions import VerifyMismatchError


SECRET_KEY = "change-this-to-a-long-random-secret"
ALGORITHM = "HS256"



hash_pass=PasswordHasher()

def has_password(password:str):
    return hash_pass.hash(password=password)

def verify_password(
    password: str,
    password_hash: str):
    return hash_pass.verify(password_hash,password) 




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