from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from app.crud.base import CRUDBase
from app.models.product import Product
from app.models.location import Location
from app.schemas.product import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):

    def get_all(self, db: Session) -> Optional[Product]:
        return db.query(Product).all()

    def get_by_type(self, db: Session, *, type: str) -> Optional[Product]:
        return db.query(Product).filter(Product.type == type).all()

    def get_products_by_location(self, db: Session, location_name: str):

        location = db.query(Location).filter(
            Location.name == location_name).first()

        if location is None:
            raise Exception(status_code=404,
                            detail=f'Location with a name {location_name} is not found')

        products = db.query(Product).join(Product.locations).filter(
            Location.name == location_name).all()

        return products

    def search(self, db: Session, query: str, limit: int, offset: int):
        search_query = f"%{query}%"

        result = db.query(Product).filter(
            or_(
                Product.name.ilike(search_query),
                Product.type.ilike(search_query)
            )
        ).limit(limit).offset(offset).all()

        filtered_products = [
            product for product in result
            if any(word.lower().startswith(query.lower()) for word in product.name.split(' '))
        ]

        sorted_products = sorted(
            filtered_products,
            key=lambda product: not any(word.lower().startswith(
                query.lower()) for word in product.name.split(' '))
        )

        return sorted_products

    def create(self, db: Session, *, obj_in: ProductCreate) -> Product:

        location_names = obj_in.locations

        db_locations = db.query(Location).filter(
            Location.name.in_(location_names)).all()

        if len(db_locations) != len(location_names):
            raise Exception(status_code=404,
                            detail='One or more locations not found')

        db_obj = Product(
            name=obj_in.name,
            type=obj_in.type,
            description=obj_in.description,
            locations=db_locations,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Product, obj_in: Union[ProductUpdate, Dict[str, Any]]
    ) -> Product:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, product_id: int) -> None:
        db_obj = db.get(Product, ident=product_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


product = CRUDProduct(Product)
