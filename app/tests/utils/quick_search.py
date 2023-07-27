from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.quick_search import QuickSearchCreate
from app.tests.utils.utils import random_lower_string


def create_random_quick_search(db: Session) -> models.QuickSearch:
    quick_search_in = QuickSearchCreate(
        name=random_lower_string()[0:8])
    return crud.quick_search.create(db=db, obj_in=quick_search_in)
