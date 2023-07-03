from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from models.feedback import Feedback
from models.response import Response

router = APIRouter()


@router.get("/feedbacks", status_code=200)
def fetch_all_feedbacks() -> Response:
    """
    Fetch all feedbacks
    """

    return Response(status=True, code=200, data=["Cool", "Awesome"])


@router.post("/feedbacks", status_code=200)
def add_suggested(feedback: Feedback) -> Response:
    """
    Add feedback to db and send in email
    """

    return Response(status=True, code=200, data=feedback)


@router.delete("/feedbacks", status_code=200)
def remove_feedback(id: str) -> Response:
    """
    Remove feedback
    """

    return Response(status=True, code=200)
