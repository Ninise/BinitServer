from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.location import Location
from schemas.location import LocationCreate, LocationUpdate


class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Location]:
        return db.query(Location).filter(Location.name == name).all()

    def get_all(self, db: Session) -> Optional[Location]:
        return db.query(Location).all()

    def create(self, db: Session, *, obj_in: LocationCreate) -> Location:

        db_obj = Location(
            name=obj_in.name
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Location, obj_in: Union[LocationUpdate, Dict[str, Any]]
    ) -> Location:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, location_id: int) -> None:
        db_obj = db.query(Location).get(location_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


location = CRUDLocation(Location)
