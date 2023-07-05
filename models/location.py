from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base
from .product import product_location_association

if TYPE_CHECKING:
    from .location import Location


class Location(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    products = relationship(
        'Product',
        secondary=product_location_association,
        back_populates='locations'
    )
