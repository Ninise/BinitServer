from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional
from fastapi.encoders import jsonable_encoder

from app.schemas.suggested import SuggestedCreate
from app.models.response import Response

from app import crud

from app.utils import deps

from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/suggested", status_code=200)
def fetch_all_suggested(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all suggested
    """

    suggested = crud.suggested.get_all(db=db)

    return Response(status=True, code=200, data=[jsonable_encoder(pr) for pr in suggested])


@router.post("/suggested", status_code=200)
def add_suggested(*, db: Session = Depends(deps.get_db), suggested_in: SuggestedCreate) -> Response:
    """
    Add suggested
    """

    suggested = crud.suggested.create(db=db, obj_in=suggested_in)

    return Response(status=True, code=200, data=suggested)


@router.delete("/suggested", status_code=200)
def remove_suggested(*, db: Session = Depends(deps.get_db), id: str) -> Response:
    """
    Remove suggested
    """

    suggested = crud.suggested.get(db, id=id)
    if suggested:
        crud.suggested.delete(db, suggested_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"Suggested product with id {id} doesn't exist")
