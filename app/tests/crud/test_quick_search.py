from sqlalchemy.orm import Session

from app import crud
from app.schemas.quick_search import QuickSearchCreate, QuickSearchUpdate
from app.tests.utils.quick_search import create_random_quick_search
from app.tests.utils.utils import random_lower_string


def test_create_quick_search(db: Session) -> None:
    name = random_lower_string()[0:8]

    quick_search_in = QuickSearchCreate(name=name)

    quick_search = crud.quick_search.create(db=db, obj_in=quick_search_in)

    assert quick_search.name == name


def test_get_quick_search(db: Session) -> None:

    quick_search = create_random_quick_search(db=db)
    stored_quick_search = crud.quick_search.get(db=db, id=quick_search.id)
    assert stored_quick_search
    assert quick_search.id == stored_quick_search.id
    assert quick_search.name == stored_quick_search.name


def test_update_quick_search(db: Session) -> None:
    quick_search = create_random_quick_search(db=db)

    created_name = quick_search.name

    quick_search_name_2 = "Snake"

    quick_search_updated = crud.quick_search.update(
        db=db, db_obj=quick_search, obj_in=QuickSearchUpdate(name=quick_search_name_2))

    assert quick_search.id == quick_search_updated.id
    assert quick_search_updated.name != created_name
    assert quick_search_name_2 == quick_search_updated.name


def test_get_all_quick_searchs(db: Session) -> None:
    create_random_quick_search(db=db)
    create_random_quick_search(db=db)
    create_random_quick_search(db=db)

    quick_searchs = crud.quick_search.get_all(db)
    assert len(quick_searchs) != 0


def test_delete_quick_search(db: Session) -> None:
    quick_search = create_random_quick_search(db=db)

    crud.quick_search.delete(db, id=quick_search.id)

    quick_search_removed = crud.quick_search.get(db, id=quick_search.id)

    assert quick_search_removed is None
