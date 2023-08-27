from sqlalchemy.orm import Session
from app import crud
from app.schemas.quiz_question import QuizQuestionCreate, QuizQuestionUpdate
from app.tests.utils.quiz_questions import create_random_quiz_question, random_quiz_question_model
from app.tests.utils.utils import random_lower_string


def test_create_quiz_question(db: Session) -> None:

    quiz_question_in = random_quiz_question_model()

    question = quiz_question_in.question
    answers = quiz_question_in.answers

    quiz_question = crud.quiz_question.create(
        db=db, obj_in=quiz_question_in)

    assert quiz_question.question == question
    assert len(quiz_question.answers) == len(answers)


def test_get_quiz_question(db: Session) -> None:

    quiz_question = create_random_quiz_question(db=db)

    stored_quiz_question = crud.quiz_question.get(
        db=db, id=quiz_question.id)

    assert stored_quiz_question
    assert quiz_question.id == stored_quiz_question.id
    assert quiz_question.question == stored_quiz_question.question


def test_update_quiz_question(db: Session) -> None:
    quiz_question = create_random_quiz_question(db=db)

    created_question = quiz_question.question

    quiz_question_question_2 = "Something is great"

    quiz_question_updated = crud.quiz_question.update(
        db=db, db_obj=quiz_question, obj_in=QuizQuestionUpdate(question=quiz_question_question_2))

    assert quiz_question.id == quiz_question_updated.id
    assert quiz_question_updated.question != created_question
    assert quiz_question_question_2 == quiz_question_updated.question


def test_delete_quiz_question(db: Session) -> None:
    quiz_question = create_random_quiz_question(db=db)

    crud.quiz_question.delete(db, quiz_question_id=quiz_question.id)

    quiz_question_removed = crud.quiz_question.get(
        db, id=quiz_question.id)

    assert quiz_question_removed is None
