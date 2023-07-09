from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from schemas.product import ProductCreate, ProductUpdate
from models.response import Response

from utils.utils import response

from sqlalchemy.orm import Session

import crud
from utils import deps

router = APIRouter()

# get all products +
# add a product +
# edit a product +
# search product +
# remove a product +
#
# suggest a product +
# remove a suggested product +
#
# game questions
#
# make a feedback request
#
# product - id, name, type, image, additional, origin, locations:[], date_added, date_updated
# suggested - id, name, type, image, additional, location
# unsuccessful_search - name, ip
# feedbacks


@router.get("/products/all", status_code=200)
def fetch_all_products(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all products
    """

    products = crud.product.get_all(db=db)

    return Response(status=True, code=200, data=products)


@router.post("/products", status_code=200)
def add_product(*, db: Session = Depends(deps.get_db), product_in: ProductCreate) -> Any:
    """
    Add a product
    """

    product = crud.product.search(db=db, query=product_in.name)
    if product:
        return Response(status=False, code=400, error=f"Product with a name {product.name} is already exists")
    else:
        product = crud.product.create(db=db, obj_in=product_in)
        return Response(status=True, code=200, data=product)


@router.put("/products", status_code=200)
def update_product(*, db: Session = Depends(deps.get_db), id: str, product_in: ProductUpdate) -> Response:
    """
    Update a product
    """

    product_exists = crud.product.get(db, id=id)
    if product_exists:
        product = crud.product.update(
            db=db, db_obj=product_exists, obj_in=product_in)

        return Response(status=True, code=200, data=product)
    else:
        return Response(status=False, code=400, error=f"Product with id {id} isn't exist")


@router.get("/products", status_code=200)
def search_products(*, db: Session = Depends(deps.get_db), query: str) -> Response:
    """
    search all products
    """

    products = crud.product.search(db, query=query)

    return Response(status=True, code=200, data=products)


@router.delete("/products", status_code=200)
def remove_product(*, db: Session = Depends(deps.get_db), id: str) -> Response:
    """
    search all products
    """

    product = crud.product.get(db, id=id)
    if product:
        crud.product.delete(db, product_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"Product with id {id} doesn't exist")
