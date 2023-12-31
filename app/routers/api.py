from fastapi import APIRouter

from app.routers import locations, feedbacks, suggests, products, articles, quick_search, garbage_category, quiz_question

api_router = APIRouter()

api_router.include_router(
    products.router, tags=["products"])

api_router.include_router(
    suggests.router, tags=["suggested"])

api_router.include_router(
    feedbacks.router, tags=["feedbacks"])

api_router.include_router(
    locations.router, tags=["locations"])

api_router.include_router(
    articles.router, tags=["articles"])

api_router.include_router(
    quick_search.router, tags=["quick_search"])

api_router.include_router(
    garbage_category.router, tags=["garbage_category"])

api_router.include_router(
    quiz_question.router, tags=["quiz_questions"])
