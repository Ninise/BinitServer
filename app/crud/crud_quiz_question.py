from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.quiz_question import QuizQuestion
from app.schemas.quiz_question import QuizQuestionCreate, QuizQuestionUpdate


class CRUDQuizQuestion(CRUDBase[QuizQuestion, QuizQuestionCreate, QuizQuestionUpdate]):
    def get_by_question(self, db: Session, *, question: str) -> Optional[QuizQuestion]:
        return db.query(QuizQuestion).filter(QuizQuestion.question == question).all()

    def get_all(self, db: Session) -> Optional[QuizQuestion]:
        return db.query(QuizQuestion).all()

    def create(self, db: Session, *, obj_in: QuizQuestionCreate) -> QuizQuestion:

        db_obj = QuizQuestion(
            question=obj_in.question,
            answers=obj_in.answers
        )

        quiz_question = db.query(QuizQuestion).filter(
            QuizQuestion.question == obj_in.question).first()

        if quiz_question is None:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        else:
            return quiz_question

    def update(
        self, db: Session, *, db_obj: QuizQuestion, obj_in: Union[QuizQuestionUpdate, Dict[str, Any]]
    ) -> QuizQuestion:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, quiz_question_id: int) -> None:
        db_obj = db.get(QuizQuestion, ident=quiz_question_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


quiz_question = CRUDQuizQuestion(QuizQuestion)
