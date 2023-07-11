from typing import Dict, Generator

import pytest
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.models import Location, Feedback, Product, Suggested
import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    # Set up the database session
    db = SessionLocal()

    # Create the table if it doesn't exist
    # Location.__table__.create(db.bind, checkfirst=True)
    # Feedback.__table__.create(db.bind, checkfirst=True)
    # Suggested.__table__.create(db.bind, checkfirst=True)
    # Product.__table__.create(db.bind, checkfirst=True)

    # Flush the table before each test
    # db.query(Location).delete()
    # db.query(Suggested).delete()
    # db.query(Product).delete()
    # db.query(Feedback).delete()
    db.commit()

    # Provide the database session to the tests
    yield db

    # Tear down the database session
    db.close()
