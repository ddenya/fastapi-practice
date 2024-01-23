from fastapi import APIRouter, status, Response, Body
from enum import Enum
from typing import Optional

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

router = APIRouter(
	prefix='/blog',
	tags=['blog']
	)

# Order is important!
# If id: int on top - it caches everything
#@router.get('/blog/all')
#def get_all_blogs():
#  return {'message':'All blogs returned'}

@router.get('/blog/all',
  tags = ['blog','comment'],
  summary='Retrieve all blogs',
  description='Api call to get all blogs',
  response_description='The list of all available blogs'
  )
def get_all_blogs(page = 1, page_size = 10):
  return {'message': f'All {page_size} blogs on page {page}'}

@router.get('/blog/{id}/comments/{comment_id}',
  tags = ['blog'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  """
  Simulates retrieving a comment

  - **id** mandatory path parameter
  - **comment_id** mandatory path parameter
  - **valid** optional query parameter
  - **username** optional query parameter
  """
  return {'message': f'blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}'}

# I can not have /blog/{type} and /blog/{id} at the same time!
# Basically /blog/{var}
@router.get('/blog/type/{type}',
  tags = ['blog'])
def get_blog_by_type(type: BlogType):
  return {'message': "Returning blog of " + type}

@router.get('/blog/{id}', 
  tags = ['blog'],
  status_code = status.HTTP_404_NOT_FOUND)
def get_blog(id: int, response: Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'message': f'hello {id}'}
  else:
    response.status_code = status.HTTP_200_OK
    return {'message': "Blog with id : " + str(id)}
