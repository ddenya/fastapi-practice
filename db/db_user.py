from sqlalchemy.orm.session import Session
from models.models import DbUser
from db.schemas import UserBase
from db.hash import Hash

def create_user(request: UserBase, db: Session):
  new_user = DbUser(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )

  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def get_all_users(db: Session):
  return db.query(DbUser).all()

def get_user(id: int, db: Session):
  return db.query(DbUser).filter(DbUser.id == id).first()

def update_user(id: int, request: UserBase, db: Session):
  user = get_user(id, db)

  user.username = request.username
  user.email = request.email
  user.password = Hash.bcrypt(request.password)

  db.commit()
  return user

def delete_user(id: int, db: Session):
  user = get_user(id, db)
  try:
    db.delete(user)
    db.commit()
  except Exception as e:
    return {'result': False} 
  return {'result': True}
