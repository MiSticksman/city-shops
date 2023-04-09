from pydantic import BaseModel
from datetime import time


class ShopBase(BaseModel):
    name: str
    house: int
    opening_time: time = "09:00:00"
    closing_time: time = "18:00:00"


class ShopCreate(ShopBase):
    city_id: int
    street_id: int


class Shop(ShopBase):
    id: int

    class Config:
        orm_mode = True
