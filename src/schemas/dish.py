from datetime import datetime

from pydantic import BaseModel


class DishCreate(BaseModel):
    name: str
    description: str
    price: float
    weight: float


class DishUpdate(BaseModel):
    price: float | None = None


class Dish(BaseModel):
    id: int
    name: str
    description: str
    price: float
    weight: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
