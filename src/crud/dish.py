from sqlalchemy import select

from database.db import async_session
from models import dish as dish_model
from schemas import dish as dish_schema


async def get_dish(dish_id: int) -> dish_model.Dish | None:
    async with async_session() as session:
        result = await session.execute(select(dish_model.Dish).filter(dish_model.Dish.id == dish_id))
        user = result.scalar_one_or_none()
        return user



async def create_dish(dish: dish_schema.DishCreate) -> dish_model.Dish:
    async with async_session() as session:
        db_dish = dish_model.Dish(**dish.model_dump())
        session.add(db_dish)
        await session.commit()
        await session.refresh(db_dish)
        return db_dish


async def update_dish(dish_id: int, dish: dish_schema.DishUpdate) -> dish_model.Dish | None:
    async with async_session() as session:
        db_dish = await get_dish(dish_id=dish_id)
        if db_dish:
            for key, value in dish.model_dump(exclude_unset=True).items():
                setattr(db_dish, key, value)
            session.add(db_dish)
            await session.commit()
            await session.refresh(db_dish)
            return db_dish
        return None


async def delete_dish(dish_id: int) -> bool:
    async with async_session() as session:
        db_dish = await get_dish(dish_id=dish_id)
        if db_dish:
            await session.delete(db_dish)
            await session.commit()
            return True
        return False
