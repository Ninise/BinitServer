from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from app.schemas.location import LocationCreate
from app.models.response import Response

from app.utils import deps

from sqlalchemy.orm import Session
from app import crud


router = APIRouter()


@router.get("/locations/all", status_code=200)
def fetch_all_locations(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all locations
    """

    locations = crud.location.get_all(db=db)

    return Response(status=True, code=200, data=locations)


@router.post("/locations", status_code=200)
def add_location(*, db: Session = Depends(deps.get_db), location_in: LocationCreate) -> Response:
    """
    Add location
    """

    location = crud.location.create(db=db, obj_in=location_in)

    return Response(status=True, code=200, data=location)


@router.delete("/location", status_code=200)
def remove_location(*, db: Session = Depends(deps.get_db), id: int) -> Response:
    """
    Remove location
    """

    location = crud.location.get(db, id=id)
    if location:
        crud.location.delete(db, location_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"Location with id {id} doesn't exist")
