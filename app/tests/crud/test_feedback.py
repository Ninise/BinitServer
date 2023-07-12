from sqlalchemy.orm import Session

from app import crud
from app.schemas.feedback import FeedbackCreate, FeedbackUpdate
from app.tests.utils.feedback import create_random_feedback
from app.tests.utils.utils import random_lower_string


def test_create_feedback(db: Session) -> None:
    message = random_lower_string()
    email = "random@email.com"

    feedback_in = FeedbackCreate(email=email, message=message)

    feedback = crud.feedback.create(db=db, obj_in=feedback_in)

    assert feedback.email == email
    assert feedback.message == message


def test_get_feedback(db: Session) -> None:

    feedback = create_random_feedback(db=db)
    stored_feedback = crud.feedback.get(db=db, id=feedback.id)
    assert stored_feedback
    assert feedback.id == stored_feedback.id
    assert feedback.message == stored_feedback.message
    assert feedback.email == stored_feedback.email


def test_update_feedback(db: Session) -> None:
    feedback = create_random_feedback(db=db)

    created_message = feedback.message

    feedback_message_2 = "Toronto is great"

    feedback_updated = crud.feedback.update(
        db=db, db_obj=feedback, obj_in=FeedbackUpdate(message=feedback_message_2))

    assert feedback.id == feedback_updated.id
    assert feedback_updated.message != created_message
    assert feedback_message_2 == feedback_updated.message


def test_get_all_feedbacks(db: Session) -> None:
    create_random_feedback(db=db)
    create_random_feedback(db=db)
    create_random_feedback(db=db)

    feedbacks = crud.feedback.get_all(db)
    assert len(feedbacks) != 0


def test_delete_feedback(db: Session) -> None:
    feedback = create_random_feedback(db=db)

    crud.feedback.delete(db, feedback_id=feedback.id)

    feedback_removed = crud.feedback.get(db, id=feedback.id)

    assert feedback_removed is None
