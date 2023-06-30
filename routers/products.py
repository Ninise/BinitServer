from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from models.product import Product
from models.response import Response

from utils.utils import response

router = APIRouter()


@router.get("/products", status_code=200, response_model=Response)
def fetch_all_products() -> Any:
    """
    Fetch all products
    """

    return response(True, 200, ["product1", "product2"])


@router.post("/products", status_code=200, response_model=Response)
def add_product() -> Any:
    """
    Add a product
    """
    # add record to db

    return response(True, 200, "addedclear")
