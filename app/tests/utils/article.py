from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.article import ArticleCreate
from app.tests.utils.utils import random_lower_string


def create_random_article(db: Session) -> models.Article:
    article_in = ArticleCreate(
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
        source="RECYCLE"
    )
    return crud.article.create(db=db, obj_in=article_in)


def random_article_model() -> ArticleCreate:
    return ArticleCreate(
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
        source="RECYCLE"
    )
