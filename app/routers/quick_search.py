from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional
from fastapi.encoders import jsonable_encoder

from app.models.quick_search import QuickSearch
from app.models.response import Response
from app.utils import deps

from sqlalchemy.orm import Session

from app import crud

from app.schemas.quick_search import QuickSearchCreate

router = APIRouter()


@router.get("/quick_search", status_code=200)
def fetch_all_quick_searches(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all QuickSearches
    """

    quickies = crud.quick_search.get_all(db=db)

    return Response(status=True, code=200, data=[jsonable_encoder(item) for item in quickies])


@router.post("/quick_search", status_code=200)
def add_quick_search(*, db: Session = Depends(deps.get_db), quick_search_in: QuickSearchCreate) -> Response:
    """
    Add quick_search to db and send in email
    """

    quick_search = crud.quick_search.create(db, obj_in=quick_search_in)
    # send email to us

    return Response(status=True, code=200, data=quick_search)


@router.delete("/quick_search", status_code=200)
def remove_quick_search(*, db: Session = Depends(deps.get_db), id: str) -> Response:
    """
    Remove quick_search
    """

    feeedback = crud.quick_search.get(db, id=id)
    if feeedback:
        crud.quick_search.delete(db=db, quick_search_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"quick_search with id {id} doesn't exist")
