from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import time, datetime

import models
import schemas


def get_shop(db: Session, shop_id: int):
    shop = db.query(models.Shop).filter(models.Shop.id == shop_id).first()
    street = db.query(models.Street).filter(models.Street.id == shop.street_id).first()
    result = ({
        'id': shop.id,
        'city_name': street.city.name,
        'street_name': street.name,
        'house': shop.house,
        'opening_time': shop.opening_time,
        'closing_time': shop.closing_time

    })
    return result


def is_shop_open(shop: schemas.Shop) -> bool:
    current_time = datetime.now().time()
    print(current_time)
    return shop.opening_time <= current_time < shop.closing_time


def get_shops(db: Session, street: str | None = None, city: str | None = None, open: str | None = None,
              skip: int = 0, limit: int = 50):
    # if street:
    #     return get_shop_by_street_name(db=db, street_name=street)
    shops = db.query(models.Shop).offset(skip).limit(limit).all()
    result = []
    for shop in shops:
        if street and not city and not open:
            if shop.street.name == street:
                result.append({
                    'id': shop.id,
                    'name': shop.name,
                    'city_name': shop.city.name,
                    'street_name': shop.street.name,
                    'house': shop.house,
                    'opening_time': shop.opening_time,
                    'closing_time': shop.closing_time
                })
        elif city and not street and not open:
            if shop.city.name == city:
                result.append({
                    'id': shop.id,
                    'name': shop.name,
                    'city_name': shop.city.name,
                    'street_name': shop.street.name,
                    'house': shop.house,
                    'opening_time': shop.opening_time,
                    'closing_time': shop.closing_time
                })
        elif open and not street and not city:
            if open == '1':
                if is_shop_open(shop):
                    result.append({
                        'id': shop.id,
                        'name': shop.name,
                        'city_name': shop.city.name,
                        'street_name': shop.street.name,
                        'house': shop.house,
                        'opening_time': shop.opening_time,
                        'closing_time': shop.closing_time
                    })
            elif open == '0':
                if not is_shop_open(shop):
                    result.append({
                        'id': shop.id,
                        'name': shop.name,
                        'city_name': shop.city.name,
                        'street_name': shop.street.name,
                        'house': shop.house,
                        'opening_time': shop.opening_time,
                        'closing_time': shop.closing_time
                    })
        elif street and city and not shop:
            if shop.street.name == street and shop.city.name == city:
                result.append({
                    'id': shop.id,
                    'name': shop.name,
                    'city_name': shop.city.name,
                    'street_name': shop.street.name,
                    'house': shop.house,
                    'opening_time': shop.opening_time,
                    'closing_time': shop.closing_time
                })
        elif street and open and not city:
            if shop.street.name == street and open == '0' and not is_shop_open(shop):
                result.append({
                    'id': shop.id,
                    'name': shop.name,
                    'city_name': shop.city.name,
                    'street_name': shop.street.name,
                    'house': shop.house,
                    'opening_time': shop.opening_time,
                    'closing_time': shop.closing_time
                })
            elif shop.street.name == street and open == '1' and is_shop_open(shop):
                result.append({
                    'id': shop.id,
                    'name': shop.name,
                    'city_name': shop.city.name,
                    'street_name': shop.street.name,
                    'house': shop.house,
                    'opening_time': shop.opening_time,
                    'closing_time': shop.closing_time
                })
        elif city and open and not street:
            if shop.city.name == city and open == '0' and not is_shop_open(shop):
                result.append({
                    'id': shop.id,
                    'name': shop.name,
                    'city_name': shop.city.name,
                    'street_name': shop.street.name,
                    'house': shop.house,
                    'opening_time': shop.opening_time,
                    'closing_time': shop.closing_time
                })
            elif shop.city.name == city and open == '1' and is_shop_open(shop):
                result.append({
                    'id': shop.id,
                    'name': shop.name,
                    'city_name': shop.city.name,
                    'street_name': shop.street.name,
                    'house': shop.house,
                    'opening_time': shop.opening_time,
                    'closing_time': shop.closing_time
                })
        elif street and city and open:
            if shop.street.name == street and shop.city.name == city:
                if open == '0':
                    check = is_shop_open(shop)
                    if not check:
                        result.append({
                            'id': shop.id,
                            'name': shop.name,
                            'city_name': shop.city.name,
                            'street_name': shop.street.name,
                            'house': shop.house,
                            'opening_time': shop.opening_time,
                            'closing_time': shop.closing_time
                        })
                elif open == '1':
                    check = is_shop_open(shop)
                    if check:
                        result.append({
                            'id': shop.id,
                            'name': shop.name,
                            'city_name': shop.city.name,
                            'street_name': shop.street.name,
                            'house': shop.house,
                            'opening_time': shop.opening_time,
                            'closing_time': shop.closing_time
                        })
        else:
            result.append({
                'id': shop.id,
                'name': shop.name,
                'city_name': shop.city.name,
                'street_name': shop.street.name,
                'house': shop.house,
                'opening_time': shop.opening_time,
                'closing_time': shop.closing_time
            })
    return result


def get_shop_by_name_and_city_id_street_id(db: Session, name: str, city_id: int, street_id: int):
    return db.query(models.Shop).filter(models.Shop.name == name,
                                        models.Shop.city_id == city_id,
                                        models.Shop.street_id == street_id).first()


# def get_shop_by_street_name(db: Session, street_name: str):
#     streets = db.query(models.Street).all()
#     shops = []
#     for street in streets:
#         if street.name == street_name:
#             shops.append(db.query(models.Shop).filter(models.Shop.street_id == street.id).first())
#     return shops
#
#
# def get_shop_by_city_name(db: Session, city_name: str):
#     cities = db.query(models.City).all()
#     shops = []
#     for city in cities:
#         if city.name == city_name:
#             shops.append(db.query(models.Shop).filter(models.Shop.city_id == city.id).first())
#     return shops


def create_shop(db: Session, shop: schemas.ShopCreate):
    db_shop = models.Shop(name=shop.name, house=shop.house, city_id=shop.city_id, street_id=shop.street_id,
                          opening_time=shop.opening_time, closing_time=shop.closing_time)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return db_shop


def delete_shop(db: Session, shop_id: int):
    shop = db.query(models.Shop).filter(models.Shop.id == shop_id).first()
    if shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    db.delete(shop)
    db.commit()
    return shop
