from fastapi import FastAPI

app=FastAPI()

#http://127.0.0.1:8000/add?a=10&b=5
@app.get('/add')
def add(a:int,b:int):
    return {"result": a + b}

@app.get('/subract')
def subract(a:int,b:int):
    return {"result": a - b}

@app.get('/multiply')
def multiplication(a:int,b:int):
    return {"result": a * b}

@app.get('/divide')
def division(a:int,b:int):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}
