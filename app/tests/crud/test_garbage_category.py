from sqlalchemy.orm import Session
from app import crud
from app.schemas.garbage_category import GarbageCategoryCreate, GarbageCategoryUpdate
from app.tests.utils.garbage_category import create_random_garbage_category, random_garbage_category_model
from app.tests.utils.utils import random_lower_string


def test_create_garbage_category(db: Session) -> None:

    garbage_category_in = random_garbage_category_model()

    title = garbage_category_in.title
    image = garbage_category_in.image
    description = garbage_category_in.description
    image_author = garbage_category_in.image_author
    image_author_url = garbage_category_in.image_author_url
    items = garbage_category_in.items
    type = garbage_category_in.type
    footer = garbage_category_in.footer

    garbage_category = crud.garbage_category.create(
        db=db, obj_in=garbage_category_in)

    assert garbage_category.title == title
    assert garbage_category.type == type
    assert garbage_category.footer == footer
    assert garbage_category.description == description
    assert garbage_category.image == image
    assert garbage_category.image_author == image_author
    assert len(garbage_category.items) == len(items)


def test_get_garbage_category(db: Session) -> None:

    garbage_category = create_random_garbage_category(db=db)

    stored_garbage_category = crud.garbage_category.get(
        db=db, id=garbage_category.id)

    assert stored_garbage_category
    assert garbage_category.id == stored_garbage_category.id
    assert garbage_category.type == stored_garbage_category.type
    assert garbage_category.description == stored_garbage_category.description


def test_update_garbage_category(db: Session) -> None:
    garbage_category = create_random_garbage_category(db=db)

    created_description = garbage_category.description

    garbage_category_description_2 = "Something is great"

    garbage_category_updated = crud.garbage_category.update(
        db=db, db_obj=garbage_category, obj_in=GarbageCategoryUpdate(description=garbage_category_description_2))

    assert garbage_category.id == garbage_category_updated.id
    assert garbage_category_updated.description != created_description
    assert garbage_category_description_2 == garbage_category_updated.description
    assert garbage_category.title == garbage_category_updated.title
    assert garbage_category.type == garbage_category_updated.type


def test_delete_garbage_category(db: Session) -> None:
    garbage_category = create_random_garbage_category(db=db)

    crud.garbage_category.delete(db, garbage_category_id=garbage_category.id)

    garbage_category_removed = crud.garbage_category.get(
        db, id=garbage_category.id)

    assert garbage_category_removed is None
