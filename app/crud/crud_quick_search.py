from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.quick_search import QuickSearch
from app.schemas.quick_search import QuickSearchCreate, QuickSearchUpdate


class CRUDQuickSearch(CRUDBase[QuickSearch, QuickSearchCreate, QuickSearchUpdate]):
    def get_all(self, db: Session) -> Optional[QuickSearch]:
        return db.query(QuickSearch).all()

    def create(self, db: Session, *, obj_in: QuickSearchCreate) -> QuickSearch:

        db_obj = QuickSearch(
            name=obj_in.name
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> None:
        db_obj = db.get(QuickSearch, ident=id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


quick_search = CRUDQuickSearch(QuickSearch)
