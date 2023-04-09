from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.crud_street
import schemas
from api.deps import get_db
router = APIRouter()

@router.get('/streets')
def get_all_streets(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    streets = crud.crud_street.get_streets(db, skip, limit)
    return streets


@router.get('/streets/{street_id}')
def get_street(street_id: int, db: Session = Depends(get_db)):
    db_street = crud.crud_street.get_street(db, street_id)
    if db_street is None:
        raise HTTPException(status_code=404, detail="Street not found")
    return db_street



@router.post('/streets', response_model=schemas.Street)
def create_street(street: schemas.StreetCreate, db: Session = Depends(get_db)):
    db_street = crud.crud_street.get_street_by_name_and_city_id(db, name=street.name, city_id=street.city_id)
    if db_street:
        raise HTTPException(status_code=400, detail="Street already registered")
    return crud.crud_street.create_street(db=db, street=street)


@router.delete('/streets/{street_id}', response_model=schemas.Street)
def delete_city(street_id: int, db: Session = Depends(get_db)):
    return crud.crud_street.delete_street(db=db, street_id=street_id)
