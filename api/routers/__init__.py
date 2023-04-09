from fastapi import APIRouter

from api.routers import shop_router, city_router, street_router

router = APIRouter()

router.include_router(city_router.router)
router.include_router(street_router.router)
router.include_router(shop_router.router)