from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base_class import Base

if TYPE_CHECKING:
    from .quiz_question import QuizQuestion


class QuizQuestion(Base):
    __tablename__ = 'quiz_question'

    id = Column(Integer, primary_key=True)
    question = Column(String, index=True)
    answers = Column(JSONB)
