from fastapi import FastAPI
from enum import Enum
from typing import Optional

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

app = FastAPI()

@app.get('/hello')
def index():
  return {'message': "Hello World!"}

@app.post('/hello')
def index2():
  return 'Hi'

# Order is important!
# If id: int on top - it caches everything
#@app.get('/blog/all')
#def get_all_blogs():
#  return {'message':'All blogs returned'}

@app.get('/blog/all')
def get_all_blogs(page = 1, page_size = 10):
  return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  return {'message': f'blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}'}

@app.get('/blog/{type}')
def get_blog_by_type(type: BlogType):
  return {'message': "Returning blog of " + type}

@app.get('/blog/{id}')
def get_blog(id: int):
  return {'message': "Blog with id : " + str(id)}
