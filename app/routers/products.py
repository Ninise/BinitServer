from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from app.schemas.product import ProductCreate, ProductUpdate
from app.models.response import Response
from fastapi.responses import JSONResponse

from app.utils.utils import response

from sqlalchemy.orm import Session

from app import crud
from app.utils import deps

router = APIRouter()


@router.get("/products/all", status_code=200)
def fetch_all_products(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all products
    """

    products = crud.product.get_all(db=db)

    return Response(status=True, code=200, data=[jsonable_encoder(pr) for pr in products])


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
def search_products(*, db: Session = Depends(deps.get_db), query: str, limit: int, offset: int) -> Response:
    """
    search all products
    """

    products = crud.product.search(db, query=query, limit=limit, offset=offset)

    return Response(status=True, code=200, data=[jsonable_encoder(pr) for pr in products])


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
