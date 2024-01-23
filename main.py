from fastapi import FastAPI
from router import blog_get

app = FastAPI()
app.include_router(blog_get.router)

@app.get('/hello')
def index():
  return {'message': "Hello World!"}

@app.post('/hello')
def index2():
  return 'Hi'


