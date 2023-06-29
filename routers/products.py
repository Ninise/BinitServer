from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional


router = APIRouter()


@router.get("/products", status_code=200)
def fetch_all_products() -> Any:
    """
    Fetch all products
    """

    return {
        "success": True,
        "code": 200,
        "data": [
            "product1", "product2", "product3",
        ]
    }
