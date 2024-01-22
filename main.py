from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
  return {'message': "Hello World!"}

@app.post('/hello')
def index2():
  return 'Hi'

@app.get('/blog/{id}')
def get_blog(id):
  return {'message': "Blog with id : " + str(id)}