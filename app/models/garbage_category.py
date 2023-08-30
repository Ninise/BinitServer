from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base_class import Base

if TYPE_CHECKING:
    from .garbage_category import GarbageCategory


class GarbageCategory(Base):
    __tablename__ = 'garbage_categories'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    image = Column(String)
    image_author = Column(String)
    image_author_url = Column(String)
    description = Column(String)
    display_type = Column(String)
    items = Column(JSONB)
    footer = Column(String)
    type = Column(String)
