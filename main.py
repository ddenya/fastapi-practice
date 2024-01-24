from fastapi import FastAPI
from router import blog_get
from router import blog_post
from models import models
from db.db_connector import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
  return {'message': "Hello World!"}

models.Base.metadata.create_all(engine)


