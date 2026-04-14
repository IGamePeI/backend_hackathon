from fastapi import APIRouter

from api import auth, dishes, orders, users

main_router = APIRouter()

main_router.include_router(users.router)
main_router.include_router(dishes.router)
main_router.include_router(orders.router)
main_router.include_router(auth.router)
