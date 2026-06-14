from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "super-secret-key-change-later"
ALGORITHM = "HS256"


def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)

    payload.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def decode_access_token(token:str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None
