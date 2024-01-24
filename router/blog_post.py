from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

class Image(BaseModel):
	url: str
	alias: str

class BlogModel(BaseModel):
	title: str # Ints are converted to str automatically
	content: str
	nb_comments: int
	published: Optional[bool]
	tags: List[str]
	metadata: Dict[str, str] = {
	'key1':'val1',
	'key2':'val2'
	}
	image: Optional[Image] = None

router = APIRouter(
	prefix='/blog',
	tags=['blog']
	)

# Path parameter
@router.post('/new/{id}')
# Query parameters
def create_blog(blog: BlogModel,
	id: int,
	version: int = 1
	):
	return {
	'id': id,
	'data': blog,
	'version': version}

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel,
	# Required because it is a path parameter
	id: int,
	comment_title: str = Query(None,
		title='Title of the comment',
		description='Some description for comment_title',
		# If I want to add alias for field name
		alias='commentTitle',
		# deprecation
		deprecated=True),
	# Ellipsis - > (...) -> eval to Ellipsis
	# Makes field required
	content: str = Body(...,
		min_length=8,
		max_length=60,
		regex='^[a-z\s]*$'),
	version: List[str] = Query(['1.0','1.2','1.4']),
	comment_id: int = Path(..., gt=5, le=10)
	):
	return {
		'blog': blog,
		'id': id,
		'comment_title': comment_title,
		'content': content,
		'version': version,
		'comment_id': comment_id
	}

def required_functionality():
	return {'message': 'Learning FastAPI is important...'}
