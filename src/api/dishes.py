from fastapi import APIRouter, HTTPException

from crud import dish as dish_crud
from schemas import dish as dish_schema

router = APIRouter(prefix="/dishes", tags=["dishes"])


@router.post("/", response_model=dish_schema.Dish, status_code=201)
async def create_dish(dish: dish_schema.DishCreate):
    return await dish_crud.create_dish(dish=dish)


@router.get("/{dish_id}", response_model=dish_schema.Dish)
async def read_dish(dish_id: int):
    db_dish = await dish_crud.get_dish(dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return db_dish

@router.get("/dishes/all")
async def get_dishes():
    dishes = await dish_crud.get_dishes()
    return dishes


@router.patch("/{dish_id}", response_model=dish_schema.Dish)
async def update_dish(dish_id: int, dish: dish_schema.DishUpdate):
    updated_dish = await dish_crud.update_dish(dish_id=dish_id, dish=dish)
    if updated_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return updated_dish


@router.delete("/{dish_id}", status_code=200)
async def delete_dish(dish_id: int):
    deleted = await dish_crud.delete_dish(dish_id=dish_id)
    if deleted:
        return {"succes": True}
    else:
        raise HTTPException(status_code=404, detail="dish not found")
