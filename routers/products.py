from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from models.product import Product
from models.response import Response

from utils.utils import response

router = APIRouter()

# get all products +
# add a product +
# edit a product
# search product
# remove a product
#
# suggest a product
# remove a suggested product
#
# game questions
#
# make a feedback request
#
# product - id, name, type, image, additional, origin, locations:[], date_added, date_updated
# suggested - id, name, type, image, additional, location
# unsuccessful_search - name, ip
# feedbacks


@router.get("/products", status_code=200)
def fetch_all_products() -> Response:
    """
    Fetch all products
    """

    return Response(status=True, code=200, data=["Prod1", "Prod2"])


@router.post("/products", status_code=200)
def add_product(product: Product) -> Response:
    """
    Add a product
    """
    # add record to db

    return Response(status=True, code=200, data=product)
