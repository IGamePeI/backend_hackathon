from datetime import datetime

from pydantic import BaseModel

from utils.enums import Category


class DishCreate(BaseModel):
    image_url: str
    name: str
    description: str
    price: float
    weight: float
    category: Category


class DishUpdate(BaseModel):
    price: float | None = None


class Dish(BaseModel):
    id: int
    image_url: str
    name: str
    description: str
    price: float
    weight: float
    category: Category
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
