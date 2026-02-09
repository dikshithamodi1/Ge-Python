from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator

app = FastAPI()

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: int

    @validator('password')
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

    @validator('age')
    def age_must_be_adult(cls, v):
        if v < 18:
            raise ValueError('User must be 18 or older')
        return v

@app.post("/register/")
async def register_user(user: UserRegistration):
    # Here you would normally save the user to a database
    return {"message": "User registered successfully", "user": user.dict()}
