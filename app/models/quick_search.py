from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.dialects.postgresql import JSONB

from app.db.base_class import Base

if TYPE_CHECKING:
    from .quick_search import QuickSearch


class QuickSearch(Base):
    __tablename__ = 'quick_search'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
