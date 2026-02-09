from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()#calling instance

@app.get('/blog')
def index(limit,published:bool,sort: Optional[str]=None):
    #only get 10 query parameters so for that do ?limit=10&published=true
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return{'data': f'{limit} blogs from db'}
    
@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished blogs'}

class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {f'data':f"blog is created with {blog.title}"}

#dynamic routing
@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id=id
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id=id
    return {'data':{'1','2'}}

@app.get('/about')
def about():
    return {'data':{'about page'}}