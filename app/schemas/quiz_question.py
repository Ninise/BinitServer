from typing import Optional, List, Dict, Any

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

import json


class QuizQuestionItem(BaseModel):
    question: str
    answers: List[str]

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'question': self.question,
            'answers': self.answers,

        }

# Shared properties


@dataclass
class QuizQuestionBase:
    question: str
    answers: Optional[List[Dict[str, Any]]] = None


# Properties to receive on item creation
class QuizQuestionCreate(QuizQuestionBase):
    pass


# Properties to receive on item update
class QuizQuestionUpdate(BaseModel):
    question: Optional[str] = None
    answers: Optional[List[Dict[str, Any]]] = None
