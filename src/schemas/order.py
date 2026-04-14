from datetime import datetime
from typing import List

from pydantic import BaseModel

from utils.enums import Status


class OrderCreate(BaseModel):
    user_id: int
    dishes_id: List[int]
    address: str
    status: Status


class OrderUpdate(BaseModel):
    status: Status | None = None


class Order(BaseModel):
    id: int
    user_id: int
    dishes_id: List[int]
    address: str
    status: Status
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
