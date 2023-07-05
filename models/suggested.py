from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .suggested import Suggested


class Suggested(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    description = Column(String, index=True)
    location = Column(String, index=True)
