from sqlalchemy.orm.session import Session
from models.models import DbUser
from db.schemas import UserBase
from db.hash import Hash

def create_user(db: Session, request: UserBase):
  new_user = DbUser(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )

  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user