from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.crud_shop
import schemas


from api.deps import get_db
router = APIRouter()

@router.get('/shops')
def get_all_shops(db: Session = Depends(get_db), skip: int = 0, limit: int = 50,
                  street: str | None = None, city: str | None = None, open: str | None = None):
    shops = crud.crud_shop.get_shops(db=db, street=street, city=city, open=open, skip=skip, limit=limit)
    return shops


@router.get('/shops/{shop_id}')
def get_shop(shop_id: int, db: Session = Depends(get_db)):
    db_shop = crud.crud_shop.get_shop(db, shop_id)
    if db_shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return db_shop



@router.post('/shops', response_model=schemas.Shop)
def create_shop(shop: schemas.ShopCreate, db: Session = Depends(get_db)):
    db_shop = crud.crud_shop.get_shop_by_name_and_city_id_street_id(db, name=shop.name, city_id=shop.city_id, street_id=shop.street_id)
    if db_shop:
        raise HTTPException(status_code=400, detail="Shop already registered")
    return crud.crud_shop.create_shop(db=db, shop=shop)


@router.delete('/shops/{shop_id}', response_model=schemas.Shop)
def delete_chop(shop_id: int, db: Session = Depends(get_db)):
    return crud.crud_shop.delete_shop(db=db, shop_id=shop_id)