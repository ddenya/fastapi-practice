from typing import List
from fastapi import APIRouter, Depends
from db.schemas import ArticleBase, ArticleDisplay
from db.db_connector import get_db
from sqlalchemy.orm import Session
from db import db_article

router = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session=Depends(get_db)):
  try:
    return db_article.create_article(request, db)
  except Exception as e:
    return {'result': False}

# Get article
@router.get('/{id}',response_model=ArticleDisplay)
def get_article(id: int, db: Session=Depends(get_db)):
  try:
    return db_article.get_article(id, db)
  except Exception as e:
    return {}

# Get all articles
@router.get('/', response_model=List[ArticleDisplay])
def get_all_articles(db: Session=Depends(get_db)):
  try:
    return db_article.get_all_articles(db)
  except Exception as e:
    return {}
  
# Update article
@router.post('/{id}', response_model=ArticleDisplay)
def update_article(id: int, request: ArticleBase, db: Session=Depends(get_db)):
  try:
    article = db_article.update_article(id, request, db)
    print(article)
    return article
  except Exception as e:
    return {}

# Delete article
@router.delete('/{id}')
def delete_article(id: int, db: Session=Depends(get_db)):
  return db_article.delete_article(id, db)