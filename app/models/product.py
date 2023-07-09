from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product

product_location_association = Table(
    'product_location_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('location_id', Integer, ForeignKey('locations.id'))
)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    description = Column(String, index=True)
    locations = relationship(
        'Location',
        secondary=product_location_association,
        back_populates='products'
    )
