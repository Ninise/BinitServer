from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from app.crud.base import CRUDBase
from app.models.product import Product
from app.models.location import Location
from app.schemas.product import ProductCreate, ProductUpdate
from sqlalchemy.sql import func


from app.utils.utils import is_garbage_type


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

        print(f'${search_query} query')
        # check if it's search by type
        if (is_garbage_type(type=query.lower())):
            print(f'${query.lower()} is garbage type')
            result = db.query(Product).filter(func.lower(Product.type).ilike(
                search_query)).limit(limit).offset(offset).all()
            return result

        # check if a search query more than 1 word
        if len(query.split(' ')) > 1:
            result = db.query(Product).filter(
                Product.name.ilike(search_query)).all()
            return result

        # in all other cases do a regular search
        result = db.query(Product).all()

        print("any other case")

        filtered_products = [
            product for product in result
            if any(word.lower().startswith(query.lower()) for word in product.name.split(' '))
        ]

        def custom_sort_key(product):
            name_parts = product.name.lower().split()
            if name_parts[0].startswith(query):
                return (0, name_parts)
            return (1, name_parts)

        sorted_products = sorted(filtered_products, key=custom_sort_key)

        return sorted_products[offset:offset + limit]

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
