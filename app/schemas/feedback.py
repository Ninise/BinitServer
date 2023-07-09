from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class FeedbackBase(BaseModel):
    email: Optional[str] = None
    message: str

# Properties to receive on item creation


class FeedbackCreate(FeedbackBase):
    pass


# Properties to receive on item update
class FeedbackUpdate(FeedbackBase):
    pass
