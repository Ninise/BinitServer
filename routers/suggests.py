from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional

from models.suggested import Suggested
from models.response import Response

router = APIRouter()


@router.get("/suggested/all", status_code=200)
def fetch_all_suggested() -> Response:
    """
    Fetch all suggested
    """

    return Response(status=True, code=200, data=["Suggested1", "Suggested2"])


@router.post("/suggested", status_code=200)
def add_suggested(suggested: Suggested) -> Response:
    """
    Add suggested
    """

    return Response(status=True, code=200, data=suggested)


@router.delete("/suggested", status_code=200)
def remove_suggested(id: str) -> Response:
    """
    Remove suggested
    """

    return Response(status=True, code=200)
