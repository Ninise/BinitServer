from fastapi import APIRouter

from routers import locations, feedbacks, suggests, products

api_router = APIRouter()

api_router.include_router(
    products.router, tags=["products"])

api_router.include_router(
    suggests.router, tags=["suggested"])

api_router.include_router(
    feedbacks.router, tags=["feedbacks"])

api_router.include_router(
    locations.router, tags=["locations"])
