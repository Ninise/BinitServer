from sqlalchemy.orm import Session

from app import crud
from app.schemas.suggested import SuggestedCreate, SuggestedUpdate
from app.tests.utils.suggested import create_random_suggested
from app.tests.utils.utils import random_lower_string


def test_create_suggested(db: Session) -> None:

    suggested_in = create_random_suggested(db=db)

    name = suggested_in.name
    location = suggested_in.location
    description = suggested_in.description
    type = suggested_in.type

    suggested = crud.suggested.create(db=db, obj_in=suggested_in)

    assert suggested.name == name
    assert suggested.location == location
    assert suggested.description == description
    assert suggested.type == type


def test_get_suggested(db: Session) -> None:

    suggested = create_random_suggested(db=db)
    stored_suggested = crud.suggested.get(db=db, id=suggested.id)
    assert stored_suggested
    assert suggested.id == stored_suggested.id
    assert suggested.type == stored_suggested.type
    assert suggested.description == stored_suggested.description


def test_update_suggested(db: Session) -> None:
    suggested = create_random_suggested(db=db)

    created_description = suggested.description

    suggested_description_2 = "Something is great"

    suggested_updated = crud.suggested.update(
        db=db, db_obj=suggested, obj_in=SuggestedUpdate(description=suggested_description_2))

    assert suggested.id == suggested_updated.id
    assert suggested_updated.description != created_description
    assert suggested_description_2 == suggested_updated.description
    assert suggested.name == suggested_updated.name
    assert suggested.type == suggested_updated.type


def test_delete_suggested(db: Session) -> None:
    suggested = create_random_suggested(db=db)

    crud.suggested.delete(db, suggested_id=suggested.id)

    suggested_removed = crud.suggested.get(db, id=suggested.id)

    assert suggested_removed is None
