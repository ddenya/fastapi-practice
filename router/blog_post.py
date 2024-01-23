from fastapi import APIRouter
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

