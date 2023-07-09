from sqlalchemy.orm import Session

from app import crud
from app.schemas.location import LocationCreate, LocationUpdate
from app.tests.utils.location import create_random_location
from app.tests.utils.utils import random_city


def test_create_location(db: Session) -> None:
    name = random_city()

    location_in = LocationCreate(name=name)

    location = crud.location.create(db=db, obj_in=location_in)

    assert location.name == name


def test_get_location(db: Session) -> None:

    location = create_random_location(db=db)
    stored_location = crud.location.get(db=db, id=location.id)
    assert stored_location
    assert location.id == stored_location.id
    assert location.name == stored_location.name


def test_update_location(db: Session) -> None:
    location = create_random_location(db=db)

    created_name = location.name

    location_name_2 = "Kyiv"

    location_updated = crud.location.update(
        db=db, db_obj=location, obj_in=LocationUpdate(name=location_name_2))

    assert location.id == location_updated.id
    assert location_updated.name != created_name
    assert location_name_2 == location_updated.name


def test_delete_location(db: Session) -> None:
    location = create_random_location(db=db)

    crud.location.delete(db, location_id=location.id)

    location_removed = crud.location.get(db, id=location.id)

    assert location_removed is None
