from fastapi import FastAPI
from enum import Enum

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
def get_all_blogs(page, page_size):
  return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/{type}')
def get_blog_by_type(type: BlogType):
  return {'message': "Returning blog of " + type}

@app.get('/blog/{id}')
def get_blog(id: int):
  return {'message': "Blog with id : " + str(id)}
