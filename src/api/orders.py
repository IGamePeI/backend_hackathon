from fastapi import APIRouter, HTTPException

from crud import order as order_crud
from schemas import order as order_schema

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=order_schema.Order, status_code=201)
async def create_order(order: order_schema.OrderCreate):
    return await order_crud.create_order(order=order)


@router.get("/{order_id}", response_model=order_schema.Order)
async def read_order(order_id: int):
    db_order = await order_crud.get_order(order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="order not found")
    return db_order


@router.patch("/{order_id}", response_model=order_schema.Order)
async def update_order(order_id: int, order: order_schema.OrderUpdate):
    updated_order = await order_crud.update_order(order_id=order_id, order=order)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="order not found")
    return updated_order


@router.delete("/{order_id}", status_code=204)
async def delete_order(order_id: int):
    deleted = await order_crud.delete_order(order_id=order_id)
    if deleted:
        return {"succes": True}
    else:
        raise HTTPException(status_code=404, detail="order not found")


@router.get("/user/{user_id}", response_model=list[order_schema.Order])
async def read_orders_by_user(user_id: int):
    orders = await order_crud.get_orders_by_user(user_id=user_id)
    return orders
