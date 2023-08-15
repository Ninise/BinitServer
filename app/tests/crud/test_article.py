from sqlalchemy.orm import Session
from app import crud
from app.schemas.article import ArticleCreate, ArticleUpdate
from app.tests.utils.article import create_random_article, random_article_model
from app.tests.utils.utils import random_lower_string


def test_create_article(db: Session) -> None:

    article_in = random_article_model()

    title = article_in.title
    image = article_in.image
    description = article_in.description
    image_author = article_in.image_author
    items = article_in.items
    source = article_in.source
    footer = article_in.footer
    type = article_in.type
    short_desc = article_in.short_description

    article = crud.article.create(db=db, obj_in=article_in)

    assert article.title == title
    assert article.source == source
    assert article.description == description
    assert article.image == image
    assert article.image_author == image_author
    assert len(article.items) == len(items)


def test_get_article(db: Session) -> None:

    article = create_random_article(db=db)

    stored_article = crud.article.get(db=db, id=article.id)

    assert stored_article
    assert article.id == stored_article.id
    assert article.source == stored_article.source
    assert article.description == stored_article.description


def test_update_article(db: Session) -> None:
    article = create_random_article(db=db)

    created_description = article.description

    article_description_2 = "Something is great"

    article_updated = crud.article.update(
        db=db, db_obj=article, obj_in=ArticleUpdate(description=article_description_2))

    assert article.id == article_updated.id
    assert article_updated.description != created_description
    assert article_description_2 == article_updated.description
    assert article.title == article_updated.title
    assert article.source == article_updated.source


def test_delete_article(db: Session) -> None:
    article = create_random_article(db=db)

    crud.article.delete(db, article_id=article.id)

    article_removed = crud.article.get(db, id=article.id)

    assert article_removed is None
