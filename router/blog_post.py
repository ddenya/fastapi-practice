from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional

class BlogModel(BaseModel):
	title: str # Ints are converted to str automatically
	content: str
	nb_comments: int
	published: Optional[bool]

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

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel,
	# Required because it is a path parameter
	id: int,
	comment_id: int = Query(None,
		title='Id of the comment',
		description='Some description for comment_id',
		# If I want to add alias for field name
		alias='commentId',
		# deprecation
		deprecated=True),
	# Ellipsis - > (...) -> eval to Ellipsis
	# Makes field required
	content: str = Body(...,
		min_length=8,
		max_length=60,
		regex='^[a-z\s]*$')
	):
	return {
		'blog': blog,
		'id': id,
		'comment_id': comment_id,
		'content': content
	}
