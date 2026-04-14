from fastapi import APIRouter, HTTPException

from crud import user as user_crud
from schemas import user as user_schema

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=user_schema.User, status_code=201)
async def create_user(user: user_schema.UserCreate):
    db_user = await user_crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await user_crud.create_user(user=user)


@router.get("/{user_id}", response_model=user_schema.User)
async def read_user(user_id: int):
    db_user = await user_crud.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.patch("/{user_id}", response_model=user_schema.User)
async def update_user(user_id: int, user: user_schema.UserUpdate):
    updated_user = await user_crud.update_user(user_id=user_id, user=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/{user_id}", status_code=200)
async def delete_user(user_id: int):
    deleted = await user_crud.delete_user(user_id=user_id)
    if deleted:
        return {"succes": True}
    else:
        raise HTTPException(status_code=404, detail="User not found")
