from fastapi import Depends
from typing import Optional

from pydantic import BaseModel

# from .city import City


class StreetBase(BaseModel):
    name: str



class StreetCreate(StreetBase):
    city_id: Optional[int]


class Street(StreetBase):
    id: int

    class Config:
        orm_mode = True
