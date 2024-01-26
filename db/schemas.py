from typing import List
from pydantic import BaseModel

# Article schema? model?
# Article inside UserDisplay (only for UserDisplay)
class Article(BaseModel):
  title: str
  content: str
  published: bool
  class Config():
    orm_mode=True

# Data we receive from user
class UserBase(BaseModel):
  username: str
  email: str
  password: str

# Data we display to user
class UserDisplay(BaseModel):
  username: str
  email: str
  items: List[Article] = []
  class Config():
    orm_mode=True

class ArticleBase(BaseModel):
  title: str
  content: str
  published: bool
  creator_id: int

# User inside ArticleDisplay
class User(BaseModel):
  id: int
  username : str
  class Config():
    orm_mode=True

# Data we display to user
class ArticleDisplay(BaseModel):
  title: str
  content: str
  published: bool
  user: User
  class Config():
    orm_mode=True

