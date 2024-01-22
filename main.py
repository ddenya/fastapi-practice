from fastapi import FastAPI, status, Response
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

@app.get('/blog/all',
  tags = ['blog','comment']
  )
def get_all_blogs(page = 1, page_size = 10):
  return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}',
  tags = ['blog'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  return {'message': f'blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}'}

# I can not have /blog/{type} and /blog/{id} at the same time!
# Basically /blog/{var}
@app.get('/blog/type/{type}',
  tags = ['blog'])
def get_blog_by_type(type: BlogType):
  return {'message': "Returning blog of " + type}

@app.get('/blog/{id}', 
  tags = ['blog'],
  status_code = status.HTTP_404_NOT_FOUND)
def get_blog(id: int, response: Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'message': f'Blog with {id} not found'}
  else:
    response.status_code = status.HTTP_200_OK
    return {'message': "Blog with id : " + str(id)}
