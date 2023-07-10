from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.feedback import FeedbackCreate
from app.tests.utils.utils import random_lower_string


def create_random_feedback(db: Session) -> models.Feedback:
    feedback_in = FeedbackCreate(
        email="random@email.com", message=random_lower_string())
    return crud.feedback.create(db=db, obj_in=feedback_in)
