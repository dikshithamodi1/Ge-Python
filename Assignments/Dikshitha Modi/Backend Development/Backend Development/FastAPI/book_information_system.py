from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
books_db=[]

class Book(BaseModel):
    title:str
    author:str
    year:int
    isbn:str

@app.post("/books/")
def add_books(book:Book):
    books_db.append(book)
    return book

@app.get("/books/")
def show(book:Book):
    return books_db