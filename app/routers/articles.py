from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Any, Optional, Dict
from fastapi.encoders import jsonable_encoder

from app.models.article import Article
from app.models.response import Response
from app.utils import deps

from sqlalchemy.orm import Session

from app import crud

from app.schemas.article import ArticleCreate

router = APIRouter()


@router.get("/articles", status_code=200)
def fetch_all_articles(*, db: Session = Depends(deps.get_db)) -> Response:
    """
    Fetch all articles
    """

    articles = crud.article.get_all(db=db)

    return Response(status=True, code=200, data=[jsonable_encoder(item) for item in articles])


@router.post("/articles", status_code=200)
def add_article(*, db: Session = Depends(deps.get_db), article_in: ArticleCreate) -> Response:
    """
    Add article to db and send in email
    """
    article = crud.article.create(db, obj_in=article_in)
    # send email to us

    return Response(status=True, code=200, data=jsonable_encoder(article))


@router.delete("/articles", status_code=200)
def remove_article(*, db: Session = Depends(deps.get_db), id: str) -> Response:
    """
    Remove article
    """

    article = crud.article.get(db, id=id)
    if article:
        crud.article.delete(db=db, article_id=id)
        return Response(status=True, code=200)
    else:
        return Response(status=False, code=400, error=f"article with id {id} doesn't exist")
