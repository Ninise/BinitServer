from typing import Optional, List, Dict, Any

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

import json


class ArticleItem(BaseModel):
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
class ArticleBase:
    title: str
    image: str
    image_author: str
    description: str
    source: str
    short_description: str
    type: str
    items: Optional[List[Dict[str, Any]]] = None
    footer: Optional[str] = None


# Properties to receive on item creation
class ArticleCreate(ArticleBase):
    pass


# Properties to receive on item update
class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    image_author: Optional[str] = None
    description: Optional[str] = None
    source: Optional[str] = None
    items: Optional[List[Dict[str, Any]]] = None
    short_description: Optional[str] = None
    footer: Optional[str] = None
    type: Optional[str] = None
