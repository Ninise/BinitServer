from sqlalchemy.orm import Session

from sqlalchemy import create_engine, MetaData

# from app import crud, schemas
from app.core.config import settings
from app.db.base import Base
from app import crud
from app import schemas


def init_db(db: Session) -> None:

    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(bind=engine)

    locations = crud.location.get_all(db)
    if not locations:
        location_in = schemas.LocationCreate(
            name="Toronto"
        )
        location = crud.location.create(db, obj_in=location_in)
