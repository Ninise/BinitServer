from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from app.models.feedback import Feedback
from app.models.response import Response
from app.utils import deps

from sqlalchemy.orm import Session

from app import crud

from app.schemas.feedback import FeedbackCreate

router = APIRouter()


@router.get("/feedbacks", status_code=200)
def fetch_all_feedbacks(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all feedbacks
    """

    feedbacks = crud.feedback.get_all(db=db)

    return Response(status=True, code=200, data=feedbacks)


@router.post("/feedbacks", status_code=200)
def add_feedback(*, db: Session = Depends(deps.get_db), feedback_in: FeedbackCreate) -> Response:
    """
    Add feedback to db and send in email
    """

    feedback = crud.feedback.create(db, obj_in=feedback_in)
    # send email to us

    return Response(status=True, code=200, data=feedback)


@router.delete("/feedbacks", status_code=200)
def remove_feedback(*, db: Session = Depends(deps.get_db), id: str) -> Response:
    """
    Remove feedback
    """

    feeedback = crud.feedback.get(db, id=id)
    if feeedback:
        crud.feedback.delete(db=db, feedback_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"Feedback with id {id} doesn't exist")
