from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.location import LocationCreate
from app.tests.utils.utils import random_city


def create_random_location(db: Session) -> models.Location:
    location_in = LocationCreate(name=random_city())
    return crud.location.create(db=db, obj_in=location_in)
