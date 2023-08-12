from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleUpdate


class CRUDArticle(CRUDBase[Article, ArticleCreate, ArticleUpdate]):
    def get_by_title(self, db: Session, *, title: str) -> Optional[Article]:
        return db.query(Article).filter(Article.title == title).all()

    def get_all(self, db: Session) -> Optional[Article]:
        return db.query(Article).all()

    def create(self, db: Session, *, obj_in: ArticleCreate) -> Article:

        db_obj = Article(
            title=obj_in.title,
            image=obj_in.image,
            image_author=obj_in.image_author,
            description=obj_in.description,
            items=obj_in.items,
            source=obj_in.source,
            short_description=obj_in.short_description,
            footer=obj_in.footer,
            type=obj_in.type
        )

        article = db.query(Article).filter(
            Article.title == obj_in.title).first()

        if article is None:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
            return db_obj
        else:
            return article

    def update(
        self, db: Session, *, db_obj: Article, obj_in: Union[ArticleUpdate, Dict[str, Any]]
    ) -> Article:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, article_id: int) -> None:
        db_obj = db.get(Article, ident=article_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()


article = CRUDArticle(Article)
