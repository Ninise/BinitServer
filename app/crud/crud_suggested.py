from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.crud.base import CRUDBase
from app.models.suggested import Suggested
from app.schemas.suggested import SuggestedCreate, SuggestedUpdate


class CRUDSuggested(CRUDBase[Suggested, SuggestedCreate, SuggestedUpdate]):

    def get_all(self, db: Session) -> Optional[Suggested]:
        return db.query(Suggested).all()

    def create(self, db: Session, *, obj_in: SuggestedCreate) -> Suggested:

        db_obj = Suggested(
            name=obj_in.name,
            type=obj_in.type,
            description=obj_in.description,
            location=obj_in.location,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Suggested, obj_in: Union[SuggestedUpdate, Dict[str, Any]]
    ) -> Suggested:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, suggested_id: int) -> None:
        db_obj = db.get(Suggested, ident=suggested_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


suggested = CRUDSuggested(Suggested)
