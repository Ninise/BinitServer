from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.feedback import Feedback
from schemas.feedback import FeedbackCreate, FeedbackUpdate


class CRUDFeedback(CRUDBase[Feedback, FeedbackCreate, FeedbackUpdate]):
    def get_all(self, db: Session) -> Optional[Feedback]:
        return db.query(Feedback).all()

    def create(self, db: Session, *, obj_in: FeedbackCreate) -> Feedback:

        db_obj = Feedback(
            email=obj_in.email,
            message=obj_in.message
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, feedback_id: int) -> None:
        db_obj = db.query(Feedback).get(feedback_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


feedback = CRUDFeedback(Feedback)
