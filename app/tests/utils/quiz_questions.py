from typing import Optional

from sqlalchemy.orm import Session

from app import crud
from app import models
from app.schemas.quiz_question import QuizQuestionCreate
from app.tests.utils.utils import random_lower_string


def create_random_quiz_question(db: Session) -> models.QuizQuestion:
    quiz_question_in = QuizQuestionCreate(
        question="Your possible question",
        answers=[
            {
                'answer': 'Leaving without plastic 1',
                'explanation': 'Good and long explanation 1',
                'isCorrect': True
            },
            {
                'answer': 'Leaving without plastic 2',
                'explanation': 'Good and long explanation 2',
                'isCorrect': False
            }
        ]
    )
    return crud.quiz_question.create(db=db, obj_in=quiz_question_in)


def random_quiz_question_model() -> QuizQuestionCreate:
    return QuizQuestionCreate(
        question="Your possible question",
        answers=[
            {
                'answer': 'Leaving without plastic 1',
                'explanation': 'Good and long explanation 1',
                'isCorrect': True
            },
            {
                'answer': 'Leaving without plastic 2',
                'explanation': 'Good and long explanation 2',
                'isCorrect': False
            }
        ]
    )
