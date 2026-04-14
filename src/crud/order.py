from sqlalchemy import select

from database.db import async_session
from models import order as order_model
from schemas import order as order_schema


async def get_order(order_id: int) -> order_model.Order | None:
    async with async_session() as session:
        result = await session.execute(select(order_model.Order).filter(order_model.Order.id == order_id))
        user = result.scalar_one_or_none()
        return user


async def get_orders() -> list[order_model.Order]:
    async with async_session() as session:
        result = await session.execute(select(order_model.Order))
        orders = result.scalars().all()
        return orders

async def get_orders_by_user(user_id: int) -> list[order_model.Order]:
    async with async_session() as session:
        result = await session.execute(
            select(order_model.Order).where(order_model.Order.user_id == user_id)
        )
        vacancy = result.scalars().all()
        return vacancy


async def create_order(order: order_schema.OrderCreate) -> order_model.Order:
    async with async_session() as session:
        db_order = order_model.Order(**order.model_dump())
        session.add(db_order)
        await session.commit()
        await session.refresh(db_order)
        return db_order


async def update_order(order_id: int, order: order_schema.OrderUpdate) -> order_model.Order | None:
    async with async_session() as session:
        db_order = await get_order(order_id=order_id)
        if db_order:
            for key, value in order.model_dump(exclude_unset=True).items():
                setattr(db_order, key, value)
            session.add(db_order)
            await session.commit()
            await session.refresh(db_order)
            return db_order
        return None


async def delete_order(order_id: int) -> bool:
    async with async_session() as session:
        db_order = await get_order(order_id=order_id)
        if db_order:
            await session.delete(db_order)
            await session.commit()
            return True
        return False
