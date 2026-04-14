from datetime import datetime, timezone

from authx import AuthX, AuthXConfig
from fastapi import Depends, HTTPException, Request
from jose import JWTError, jwt

from config import settings
from crud import user as crud


def get_token(request: Request):
    token = request.cookies.get(settings.USER_ACCESS_TOKEN_NAME)
    if not token:
        raise HTTPException(status_code=401, detail="Token not found")
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
    except JWTError:
        raise HTTPException(status_code=401, detail="token invalid!")  # noqa: B904
    expire = payload.get("exp")
    if expire is not None:
        expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)
        if (not expire) or (expire_time < datetime.now(timezone.utc)):
            raise HTTPException(status_code=401, detail="Token expired")
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Token invalid")
    user = await crud.get_user(int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


config = AuthXConfig()
config.JWT_SECRET_KEY = settings.SECRET_KEY
config.JWT_ACCESS_TOKEN_EXPIRES = None
config.JWT_ACCESS_COOKIE_NAME = settings.USER_ACCESS_TOKEN_NAME
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)
