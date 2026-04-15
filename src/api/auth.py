from fastapi import APIRouter, Depends, HTTPException, Response

from crud import user as user_crud
from schemas import user as schema
from utils import auth
from utils.enums import UserRole
from utils.security import verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(user: schema.UserLogin, response: Response):
    db_user = await user_crud.get_user_by_email(user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = auth.security.create_access_token(uid=str(db_user.id))
    response.set_cookie(
        auth.config.JWT_ACCESS_COOKIE_NAME,
        token,
        httponly=True,
    )
    response.set_cookie("login", True)
    return {"succes": True}


@router.get("/me", dependencies=[Depends(auth.security.access_token_required)], response_model=schema.User)
async def get_current_user(user_data: schema.User = Depends(auth.get_current_user)):  # noqa: B008
    return user_data

@router.get("/is_admin", dependencies=[Depends(auth.security.access_token_required)], response_model=schema.User)
async def is_admin(user_data: schema.User = Depends(auth.get_current_user)):  # noqa: B008
    if user_data.role == UserRole.ADMIN:
        return True
    else:
        return False

@router.get("/is_delivery", dependencies=[Depends(auth.security.access_token_required)], response_model=schema.User)
async def is_delivery(user_data: schema.User = Depends(auth.get_current_user)):  # noqa: B008
    if user_data.role == UserRole.DELIVERY_MAN:
        return True
    else:
        return False

