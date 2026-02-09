Fundoo Notes Application

A simple full-stack notes application built using FastAPI and HTML/CSS/JavaScript.

Features

User Register & Login

JWT Authentication

Forgot & Reset Password

Create, View, Update, Delete Notes

Notes are user-specific

Tech Stack

Backend: FastAPI, SQLAlchemy, SQLite

Auth: JWT, bcrypt

Frontend: HTML, CSS, JavaScript

Server: Uvicorn

How to Run
Backend
venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

Frontend

Open:

frontend/index.html


(using Live Server)

API Endpoints

POST /register

POST /login

POST /forgot-password

POST /reset-password

POST /notes

GET /notes

PUT /notes/{id}

DELETE /notes/{id}

Database

SQLite (fundoo.db)

Tables: users, notes, password_reset_tokens

Author

Dikshitha Modi