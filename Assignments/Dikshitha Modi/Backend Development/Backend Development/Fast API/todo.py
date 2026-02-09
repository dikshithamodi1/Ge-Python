from fastapi import FastAPI,HTTPException
from typing import Optional,List
from pydantic import BaseModel

app=FastAPI()

class ToDo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

#used when updating or deleting
class ToDoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks_db: List[ToDo] = []

@app.post("/todos/", status_code=201)
def create_todo(todo: ToDoCreate):
    new_id = len(tasks_db) + 1
    new_todo = ToDo(id=new_id, **todo.dict())
    tasks_db.append(new_todo)
    return new_todo

@app.get("/todos/")
def get_all_todos():
    return tasks_db

@app.get("/todos/{id}")
def get_todo(id: int):
    for todo in tasks_db:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{id}")
def update_todo(id: int, updated: ToDoCreate):
    for index, todo in enumerate(tasks_db):
        if todo.id == id:
            tasks_db[index] = ToDo(id=id, **updated.dict())
            return tasks_db[index]
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{id}")
def delete_todo(id: int):
    for index, todo in enumerate(tasks_db):
        if todo.id == id:
            tasks_db.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")