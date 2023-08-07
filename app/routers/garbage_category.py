from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional, Dict
from fastapi.encoders import jsonable_encoder

from app.models.garbage_category import GarbageCategory
from app.models.response import Response
from app.utils import deps

from sqlalchemy.orm import Session

from app import crud

from app.schemas.garbage_category import GarbageCategoryCreate

router = APIRouter()


@router.get("/garbage_categories", status_code=200)
def fetch_all_garbage_categories(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all garbage_categories
    """

    garbage_categories = crud.garbage_category.get_all(db=db)

    return Response(status=True, code=200, data=[jsonable_encoder(item) for item in garbage_categories])


@router.post("/garbage_categories", status_code=200)
def add_garbage_category(*, db: Session = Depends(deps.get_db), garbage_category_in: GarbageCategoryCreate) -> Response:
    """
    Add garbage_category to db and send in email
    """
    garbage_category = crud.garbage_category.create(
        db, obj_in=garbage_category_in)
    # send email to us

    return Response(status=True, code=200, data=jsonable_encoder(garbage_category))


@router.delete("/garbage_categories", status_code=200)
def remove_garbage_category(*, db: Session = Depends(deps.get_db), id: str) -> Response:
    """
    Remove garbage_category
    """

    garbage_category = crud.garbage_category.get(db, id=id)
    if garbage_category:
        crud.garbage_category.delete(db=db, garbage_category_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"garbage_category with id {id} doesn't exist")
