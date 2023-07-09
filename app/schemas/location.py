from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class LocationBase(BaseModel):
    name: str

# Properties to receive on item creation


class LocationCreate(LocationBase):
    pass


# Properties to receive on item update
class LocationUpdate(LocationBase):
    pass
