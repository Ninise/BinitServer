from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.garbage_category import GarbageCategoryCreate
from app.tests.utils.utils import random_lower_string


def create_random_garbage_category(db: Session) -> models.GarbageCategory:
    garbage_category_in = GarbageCategoryCreate(
        title="Great things do to without you",
        image="https://binit.cool/",
        image_author="MyCoolPic",
        description=random_lower_string(),
        items=[
            {
                'title': 'Leaving without plastic',
                'data': ["Nice", "Good", "Awesome"]
            },
            {
                'title': 'Leaving without food',
                'data': ["terrible", "aww", "poor"]
            }
        ],
        type="RECYCLE",
        footer="Cool footer"
    )
    return crud.garbage_category.create(db=db, obj_in=garbage_category_in)


def random_garbage_category_model() -> GarbageCategoryCreate:
    return GarbageCategoryCreate(
        title="Great things do to without you",
        image="https://binit.cool/",
        image_author="MyCoolPic",
        description=random_lower_string(),
        items=[
            {
              'title': 'Leaving without plastic',
              'data': ["Nice", "Good", "Awesome"]
            },
            {
                'title': 'Leaving without food',
                'data': ["terrible", "aww", "poor"]
            }
        ],
        type="RECYCLE",
        footer="Lower stuff"
    )
