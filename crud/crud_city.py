from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

import models
import schemas


def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_cities(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.City).offset(skip).limit(limit).all()


def get_city_by_name(db: Session, name: str):
    return db.query(models.City).filter(models.City.name == name).first()


def get_city_streets(db: Session, city_id: int):
    return db.query(models.Street).filter(models.Street.city_id == city_id).all()


def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(name=city.name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def delete_city(db: Session, city_id: int):
    city = db.query(models.City).filter(models.City.id == city_id).first()
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    db.delete(city)
    db.commit()
    return city
