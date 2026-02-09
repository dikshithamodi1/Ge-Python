from fastapi import FastAPI
from routes import router

app = FastAPI(title="Fundoo Notes")

app.include_router(router)
