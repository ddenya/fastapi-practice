from sqlalchemy.orm.session import Session
from db.schemas import ArticleBase
from models.models import DbArticle

# Get one article
def get_article(id: int, db: Session):
  try:
    return db.query(DbArticle).filter(DbArticle.id == id).first()
  except Exception as e:
    return {}
  
# Get all articles
def get_all_articles(db: Session):
  try:
    articles = db.query(DbArticle).all()
    return articles
  except Exception as e:
    return {}

# Create article
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
  
# Update article
def update_article(id: int, request: ArticleBase, db: Session):
  try:
    article = get_article(id, db)
    article.title = request.title
    article.content = request.content
    article.published = request.published
    db.commit()
    return article
  except Exception as e:
    return {'result': False}

# Delete article
def delete_article(id: int, db: Session):
  try:
    article = get_article(id, db)
    db.delete(article)
    db.commit()
    return {'result': True}
  except Exception as e:
    return {'result': False}
