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
    pass
