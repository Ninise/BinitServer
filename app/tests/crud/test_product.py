from sqlalchemy.orm import Session

from app import crud
from app.schemas.product import ProductCreate, ProductUpdate
from app.tests.utils.product import create_random_product
from app.tests.utils.utils import random_lower_string
from app.models.product import Product


def test_create_product(db: Session) -> None:

    product_in = create_random_product(db=db)

    name = product_in.name
    location = product_in.locations
    description = product_in.description
    type = product_in.type

    product = crud.product.create(db=db, obj_in=ProductCreate(
        name=name,
        image="soon",
        locations=[location[0].name],
        description=description,
        type=type
    ))

    assert product.name == name
    assert product.locations == location
    assert product.description == description
    assert product.type == type


def test_get_products_by_location_name(db: Session) -> None:
    location_name = "Burlington"

    create_random_product(db=db)
    create_random_product(db=db)
    create_random_product(db=db)

    products = crud.product.get_products_by_location(
        db, location_name=location_name)

    assert products.count != 0


def test_get_products_by_type(db: Session) -> None:
    type_name = "ORG"

    create_random_product(db=db)
    create_random_product(db=db)
    create_random_product(db=db)

    products = crud.product.get_by_type(
        db, type=type_name)

    assert products.count != 0


def test_get_product(db: Session) -> None:

    product = create_random_product(db=db)
    stored_product = crud.product.get(db=db, id=product.id)
    assert stored_product
    assert product.id == stored_product.id
    assert product.type == stored_product.type
    assert product.description == stored_product.description


# def test_search_type(db: Session) -> None:
#     # Define a test query
#     query = "ORG"

#     results = crud.product.search(db=db, query=query, limit=10, offset=0)

#     assert isinstance(results, list)
#     assert all(isinstance(result, Product) for result in results)


def test_search_name(db: Session) -> None:
    # Define a test query
    query = "axe"

    results = crud.product.search(db=db, query=query, limit=10, offset=0)
    print(results)
    assert results[0].name == "axe deo"
    assert len(results) == 2
    assert isinstance(results, list)
    assert all(isinstance(result, Product) for result in results)


def test_get_all_products(db: Session) -> None:
    create_random_product(db=db)
    create_random_product(db=db)
    create_random_product(db=db)

    results = crud.product.get_all(db=db)

    assert isinstance(results, list)
    assert all(isinstance(result, Product) for result in results)


def test_update_product(db: Session) -> None:
    product = create_random_product(db=db)

    created_description = product.description

    product_description_2 = "Something is great"

    product_updated = crud.product.update(
        db=db, db_obj=product, obj_in=ProductUpdate(description=product_description_2))

    assert product.id == product_updated.id
    assert product_updated.description != created_description
    assert product_description_2 == product_updated.description
    assert product.name == product_updated.name
    assert product.type == product_updated.type


def test_delete_product(db: Session) -> None:
    product = create_random_product(db=db)

    crud.product.delete(db, product_id=product.id)

    product_removed = crud.product.get(db, id=product.id)

    assert product_removed is None
