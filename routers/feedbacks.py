from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from models.feedback import Feedback
from models.response import Response
from utils.deps import deps

from sqlalchemy.orm import Session

import crud

from schemas.feedback import FeedbackCreate

router = APIRouter()


@router.get("/feedbacks", status_code=200)
def fetch_all_feedbacks() -> Response:
    """
    Fetch all feedbacks
    """

    return Response(status=True, code=200, data=["Cool", "Awesome"])


@router.post("/feedbacks", status_code=200)
def add_suggested(*, db: Session = Depends(deps.get_db), feedback_in: FeedbackCreate) -> Response:
    """
    Add feedback to db and send in email
    """

    feedback = crud.feedback.create(db, obj_in=feedback_in)

    return Response(status=True, code=200, data=feedback)


@router.delete("/feedbacks", status_code=200)
def remove_feedback(id: str) -> Response:
    """
    Remove feedback
    """

    return Response(status=True, code=200)
