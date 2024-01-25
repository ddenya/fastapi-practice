from pydantic import BaseModel

# Data we receive from user
class UserBase(BaseModel):
  username: str
  email: str
  password: str

# Data we provide to user
class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode=True