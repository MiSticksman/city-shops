
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.crud_city
import schemas
from api.deps import get_db

router = APIRouter()




@router.get('/cities', response_model=list[schemas.City])
def get_all_cities(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    cities = crud.crud_city.get_cities(db, skip, limit)
    return cities


@router.get('/cities/{city_id}', response_model=schemas.City)
def get_city(city_id: int, db: Session = Depends(get_db)):
    db_city = crud.crud_city.get_city(db, city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city


@router.get('/cities/{city_id}/streets', response_model=list[schemas.Street])
def get_city_streets(city_id: int, db: Session = Depends(get_db)):
    db_streets = crud.crud_city.get_city_streets(db, city_id)
    return db_streets


@router.post('/cities', response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    db_city = crud.crud_city.get_city_by_name(db, name=city.name)
    if db_city:
        raise HTTPException(status_code=400, detail="City already registered")
    return crud.crud_city.create_city(db=db, city=city)


@router.delete('/cities/{city_id}')
def delete_city(city_id: int, db: Session = Depends(get_db)):
    return crud.crud_city.delete_city(db=db, city_id=city_id)