from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.crud.base import CRUDBase
from app.models.product import Product
from app.models.location import Location
from app.schemas.product import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):

    def get_all(self, db: Session) -> Optional[Product]:
        return db.get(Product).all()

    def get_by_type(self, db: Session, *, type: str) -> Optional[Product]:
        return db.query(Product).filter(Product.type == type).all()

    def search(self, db: Session, query: str):
        search_query = f"%{query}%"

        return db.query(Product).filter(
            or_(
                Product.NAME.ilike(search_query),
                Product.TYPE.ilike(search_query)
            )
        ).all()

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
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, product_id: int) -> None:
        db_obj = db.get(Product, ident=product_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


product = CRUDProduct(Product)
