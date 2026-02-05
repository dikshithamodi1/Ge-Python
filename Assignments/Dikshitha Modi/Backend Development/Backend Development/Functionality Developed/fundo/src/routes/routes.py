from fastapi import APIRouter, HTTPException, Depends
import uuid

from logger import get_logger
from models import *
from database import load_data, save_data
from auth import create_access_token, get_current_user

logger = get_logger()
router = APIRouter()

# ---------------- HOME ----------------
@router.get("/")
def home():
    return {"message": "Fundoo Backend Running"}

# ---------------- REGISTER ----------------
@router.post("/register")
def register(request: RegisterRequest):
    data = load_data()

    if request.email in data["users"]:
        raise HTTPException(400, "User already exists")

    data["users"][request.email] = {
        "username": request.username,
        "password": request.password,
        "notes": []
    }

    save_data(data)
    logger.info(f"User registered {request.email}")
    return {"message": "Registered Successfully"}

# ---------------- LOGIN ----------------
@router.post("/login")
def login(request: LoginRequest):
    data = load_data()
    user = data["users"].get(request.email)

    if not user or user["password"] != request.password:
        raise HTTPException(401, "Invalid Credentials")

    token = create_access_token({"sub": request.email})
    return {"access_token": token, "token_type": "bearer"}

# ---------------- FORGOT PASSWORD ----------------
@router.post("/forgot-password")
def forgot(request: ForgotPasswordRequest):
    data = load_data()

    if request.email not in data["users"]:
        raise HTTPException(404, "User not found")

    token = str(uuid.uuid4())
    data["reset_tokens"][token] = request.email
    save_data(data)

    return {"message": f"Reset Token: {token}"}

# ---------------- RESET PASSWORD ----------------
@router.post("/reset-password")
def reset(request: ResetPasswordRequest):
    data = load_data()

    email = data["reset_tokens"].get(request.token)
    if not email:
        raise HTTPException(400, "Invalid token")

    data["users"][email]["password"] = request.new_password
    del data["reset_tokens"][request.token]
    save_data(data)

    return {"message": "Password Updated"}

# ---------------- CREATE NOTE ----------------
@router.post("/notes")
def create_note(note: NoteCreate, user: str = Depends(get_current_user)):
    data = load_data()

    note_id = str(uuid.uuid4())
    data["users"][user]["notes"].append({
        "id": note_id,
        "title": note.title,
        "content": note.content
    })

    save_data(data)
    return {"message": "Note Created", "id": note_id}

# ---------------- READ NOTES ----------------
@router.get("/notes")
def get_notes(user: str = Depends(get_current_user)):
    data = load_data()
    return data["users"][user]["notes"]

# ---------------- UPDATE NOTE ----------------
@router.put("/notes/{note_id}")
def update_note(note_id: str, note: NoteUpdate, user: str = Depends(get_current_user)):
    data = load_data()
    notes = data["users"][user]["notes"]

    for n in notes:
        if n["id"] == note_id:
            n["title"] = note.title
            n["content"] = note.content
            save_data(data)
            return {"message": "Updated"}

    raise HTTPException(404, "Note not found")

# ---------------- DELETE NOTE ----------------
@router.delete("/notes/{note_id}")
def delete_note(note_id: str, user: str = Depends(get_current_user)):
    data = load_data()
    notes = data["users"][user]["notes"]

    for n in notes:
        if n["id"] == note_id:
            notes.remove(n)
            save_data(data)
            return {"message": "Deleted"}

    raise HTTPException(404, "Note not found")
