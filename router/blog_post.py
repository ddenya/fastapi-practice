from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

class BlogModel(BaseModel):
	title: str
	content: str
	published: Optional[bool]

router = APIRouter(
	prefix='/blog',
	tags=['blog']
	)

@router.post('/new')
def create_blog(blog: BlogModel):
	return blog.title

