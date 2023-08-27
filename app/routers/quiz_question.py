from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional, Dict
from fastapi.encoders import jsonable_encoder

from app.models.quiz_question import QuizQuestion
from app.models.response import Response
from app.utils import deps

from sqlalchemy.orm import Session

from app import crud

from app.schemas.quiz_question import QuizQuestionCreate

router = APIRouter()


@router.get("/quiz_questions", status_code=200)
def fetch_all_quiz_questions(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all quiz_questions
    """

    quiz_questions = crud.quiz_question.get_all(db=db)

    return Response(status=True, code=200, data=[jsonable_encoder(item) for item in quiz_questions])


@router.post("/quiz_questions", status_code=200)
def add_quiz_questions(*, db: Session = Depends(deps.get_db), quiz_questions_in: QuizQuestionCreate) -> Response:
    """
    Add quiz_questions to db 
    """
    quiz_questions = crud.quiz_question.create(
        db, obj_in=quiz_questions_in)

    return Response(status=True, code=200, data=jsonable_encoder(quiz_questions))


@router.delete("/quiz_questions", status_code=200)
def remove_quiz_questions(*, db: Session = Depends(deps.get_db), id: str) -> Response:
    """
    Remove quiz_questions
    """

    quiz_questions = crud.quiz_question.get(db, id=id)
    if quiz_questions:
        crud.quiz_question.delete(db=db, quiz_questions_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"quiz_questions with id {id} doesn't exist")
