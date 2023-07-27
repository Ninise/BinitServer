from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class QuickSearchBase(BaseModel):
    name: str


# Properties to receive on item creation


class QuickSearchCreate(QuickSearchBase):
    pass


# Properties to receive on item update
class QuickSearchUpdate(QuickSearchBase):
    pass
