from fastapi import APIRouter

from routers import products
from routers import suggests
from routers import feedbacks


api_router = APIRouter()

api_router.include_router(
    products.router, tags=["products"])

api_router.include_router(
    suggests.router, tags=["suggested"])

api_router.include_router(
    feedbacks.router, tags=["feedbacks"])
