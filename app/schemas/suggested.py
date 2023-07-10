from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class SuggestedBase(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    location: Optional[str] = None

# Properties to receive on item creation


class SuggestedCreate(SuggestedBase):
    pass


# Properties to receive on item update
class SuggestedUpdate(SuggestedBase):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
