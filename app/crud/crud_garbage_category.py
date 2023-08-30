from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.garbage_category import GarbageCategory
from app.schemas.garbage_category import GarbageCategoryCreate, GarbageCategoryUpdate


class CRUDGarbageCategory(CRUDBase[GarbageCategory, GarbageCategoryCreate, GarbageCategoryUpdate]):
    def get_by_title(self, db: Session, *, title: str) -> Optional[GarbageCategory]:
        return db.query(GarbageCategory).filter(GarbageCategory.title == title).all()

    def get_all(self, db: Session) -> Optional[GarbageCategory]:
        return db.query(GarbageCategory).all()

    def create(self, db: Session, *, obj_in: GarbageCategoryCreate) -> GarbageCategory:

        db_obj = GarbageCategory(
            title=obj_in.title,
            image=obj_in.image,
            image_author=obj_in.image_author,
            image_author_url=obj_in.image_author_url,
            description=obj_in.description,
            items=obj_in.items,
            type=obj_in.type,
            footer=obj_in.footer,
            display_type=obj_in.display_type
        )

        garbage_category = db.query(GarbageCategory).filter(
            GarbageCategory.title == obj_in.title).first()

        if garbage_category is None:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        else:
            return garbage_category

    def update(
        self, db: Session, *, db_obj: GarbageCategory, obj_in: Union[GarbageCategoryUpdate, Dict[str, Any]]
    ) -> GarbageCategory:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, garbage_category_id: int) -> None:
        db_obj = db.get(GarbageCategory, ident=garbage_category_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


garbage_category = CRUDGarbageCategory(GarbageCategory)
