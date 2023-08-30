from typing import Optional, List, Dict, Any

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

import json


class GarbageCategoryItem(BaseModel):
    title: str
    data: List[str]

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'title': self.title,
            'data': self.data,

        }

# Shared properties


@dataclass
class GarbageCategoryBase:
    title: str
    image: str
    image_author: str
    image_author_url: str
    description: str
    display_type: str
    type: str
    footer: Optional[str] = None
    items: Optional[List[Dict[str, Any]]] = None


# Properties to receive on item creation
class GarbageCategoryCreate(GarbageCategoryBase):
    pass


# Properties to receive on item update
class GarbageCategoryUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    image_author: Optional[str] = None
    image_author_url: Optional[str] = None
    description: Optional[str] = None
    display_type: Optional[str] = None
    type: Optional[str] = None
    footer: Optional[str] = None
    items: Optional[List[Dict[str, Any]]] = None
