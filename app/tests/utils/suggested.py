from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.suggested import SuggestedCreate
from app.tests.utils.utils import random_lower_string

import random


def create_random_suggested(db: Session) -> models.Suggested:
    suggested_in = SuggestedCreate(
        name=random_lower_string(),
        type=random.choice(["ORG", "GARB", "RECY"]),
        description=random_lower_string(),
        location=random_lower_string()
    )
    return crud.suggested.create(db=db, obj_in=suggested_in)
