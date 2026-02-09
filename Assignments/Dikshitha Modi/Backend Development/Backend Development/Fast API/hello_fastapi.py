from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def message():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")
def get_name(name:str):
    return {"greeting":f"Hello, {name}!"}
