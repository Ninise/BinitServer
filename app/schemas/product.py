from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    name: str
    type: str
    description: str = None
    locations: List[str]

# Properties to receive on item creation


class ProductCreate(ProductBase):
    pass


# Properties to receive on item update
class ProductUpdate(ProductBase):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    locations: Optional[List[str]] = None
