from pydantic import BaseModel
from datetime import time

from .street import Street


class CityBase(BaseModel):
    name: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int
    streets: list[Street] = []

    class Config:
        orm_mode = True


