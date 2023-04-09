from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

import models
import schemas


def get_street(db: Session, street_id: int):
    street = db.query(models.Street).filter(models.Street.id == street_id).first()
    city = db.query(models.City).filter(models.City.id == street.city_id).first()
    result = {
        'id': street.id,
        'street_name': street.name,
        'city_name': city.name
    }
    return result



def get_streets(db: Session, skip: int = 0, limit: int = 50):
    streets = db.query(models.Street).offset(skip).limit(limit).all()
    result = []
    for street in streets:
        city = db.query(models.City).filter(models.City.id == street.city_id).first()
        result.append({
            'id': street.id,
            'street_name': street.name,
            'city_name': city.name
        })
    return result


def get_street_by_name_and_city_id(db: Session, name: str, city_id: int):
    return db.query(models.Street).filter(models.Street.name == name, models.Street.city_id == city_id).first()


def create_street(db: Session, street: schemas.StreetCreate):
    db_street = models.Street(name=street.name, city_id=street.city_id)
    db.add(db_street)
    db.commit()
    db.refresh(db_street)
    return db_street


def delete_street(db: Session, street_id: int):
    street = db.query(models.Street).filter(models.Street.id == street_id).first()
    if street is None:
        raise HTTPException(status_code=404, detail="Street not found")
    db.delete(street)
    db.commit()
    return street
