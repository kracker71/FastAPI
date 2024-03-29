from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/')
def home():
    return "home page"

@app.get('/blog')
def index(limit=10, published : bool = True, sort: Optional[str] = None):
    # only get 10 published blog
    if(published):
        return {'data': f'{limit} published blogs from the db'}
    return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unplublished():
    return {'data':'all unpublished blog'}

@app.get('/blog/{id}')
def show(id:int):
    #fetch blog wiht id = id
    return {'data':id}


@app.get('/blog/{id}/comment')
def commnet(id,limit=10):
    #fetch comment of blof id = id
    return {'data':{'1','2'}}



class Blog(BaseModel):
    title: str
    body : str
    published : Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data':f"Blog is created with title as {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app,host = '127.0.0.1', port = 9000)