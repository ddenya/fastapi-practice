from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from models.models import DbArticle

def get_article(id: int, db: Session):
  try:
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    return article
  except Exception as e:
    return {'result': False}

def create_article(request: ArticleBase, db: Session):
  try:
    new_article = DbArticle(
      title = request.title,
      content = request.content,
      published = request.published,
      user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    # To get id of a new article created?
    db.refresh(new_article)
    return new_article
  except Exception as e:
    return {'result': False}

