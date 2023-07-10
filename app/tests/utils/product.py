from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.product import ProductCreate
from app.schemas.location import LocationCreate
from app.tests.utils.utils import random_lower_string

import random


def create_random_product(db: Session) -> models.Product:
    location = crud.location.create(
        db=db, obj_in=LocationCreate(name="Toronto"))

    location2 = crud.location.create(
        db=db, obj_in=LocationCreate(name="Ottawa"))

    product_in = ProductCreate(
        name=random_lower_string(),
        type=random.choice(["ORG", "GARB", "RECY"]),
        description=random_lower_string(),
        locations=[location.name, location2.name]
    )
    return crud.product.create(db=db, obj_in=product_in)
