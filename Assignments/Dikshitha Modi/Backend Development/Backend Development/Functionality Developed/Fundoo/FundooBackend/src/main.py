import uuid
from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# ---------- LOGGER ----------
from logger import get_logger
logger = get_logger("fundoo_backend")

# ---------- DB & MODELS ----------
from database import Base, engine, get_db
from models import User, Note, PasswordResetToken
from schemas import (
    RegisterRequest,
    LoginRequest,
    NoteCreate,
    ForgotPasswordRequest,
    ResetPasswordRequest
)
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    decode_token
)

# ---------- APP ----------
app = FastAPI(title="Fundoo Notes API")

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- CREATE TABLES ON STARTUP ----------
@app.on_event("startup")
def startup():
    logger.info("Starting application and creating tables if not exist")
    Base.metadata.create_all(bind=engine)

# ---------- AUTH HELPER ----------
def get_current_user(
    token: str = Header(...),
    db: Session = Depends(get_db)
):
    logger.info("Validating token")
    payload = decode_token(token)
    user = db.query(User).filter(User.id == payload["user_id"]).first()
    if not user:
        logger.error("Invalid token used")
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

# ---------- REGISTER ----------
@app.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    logger.info(f"Register attempt: {data.email}")

    if db.query(User).filter(User.email == data.email).first():
        logger.warning(f"User already exists: {data.email}")
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        email=data.email,
        password=hash_password(data.password)
    )
    db.add(user)
    db.commit()

    logger.info(f"User registered successfully: {data.email}")
    return {"message": "User registered successfully"}

# ---------- LOGIN ----------
@app.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    logger.info(f"Login attempt: {data.email}")

    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        logger.error(f"Invalid login for {data.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    logger.info(f"Login successful: {data.email}")

    return {"access_token": token}

# ---------- NOTES CRUD ----------
@app.post("/notes")
def add_note(
    note: NoteCreate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    logger.info(f"User {user.id} creating note: {note.title}")

    new_note = Note(
        title=note.title,
        content=note.content,
        user_id=user.id
    )
    db.add(new_note)
    db.commit()

    logger.info(f"Note created with ID {new_note.id}")
    return {"message": "Note added"}

@app.get("/notes")
def get_notes(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    logger.info(f"User {user.id} fetching notes")
    return db.query(Note).filter(Note.user_id == user.id).all()

@app.put("/notes/{note_id}")
def update_note(
    note_id: int,
    note: NoteCreate,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    logger.info(f"User {user.id} updating note {note_id}")

    db_note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == user.id
    ).first()

    if not db_note:
        logger.warning(f"Note not found: {note_id}")
        raise HTTPException(status_code=404, detail="Note not found")

    db_note.title = note.title
    db_note.content = note.content
    db.commit()

    logger.info(f"Note updated: {note_id}")
    return {"message": "Note updated"}

@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    logger.info(f"User {user.id} deleting note {note_id}")

    db_note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == user.id
    ).first()

    if not db_note:
        logger.warning(f"Note not found: {note_id}")
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(db_note)
    db.commit()

    logger.info(f"Note deleted: {note_id}")
    return {"message": "Note deleted"}

# ---------- FORGOT PASSWORD ----------
@app.post("/forgot-password")
def forgot_password(
    data: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    logger.info(f"Forgot password request: {data.email}")

    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        logger.error("User not found for forgot password")
        raise HTTPException(status_code=404, detail="User not found")

    token = str(uuid.uuid4())
    reset = PasswordResetToken(token=token, user_id=user.id)
    db.add(reset)
    db.commit()

    logger.info(f"Reset token generated for user {user.id}")
    return {
        "message": "Reset token generated",
        "reset_token": token  # dev/testing only
    }

# ---------- RESET PASSWORD ----------
@app.post("/reset-password")
def reset_password(
    data: ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    logger.info("Reset password attempt")

    reset_entry = db.query(PasswordResetToken).filter(
        PasswordResetToken.token == data.token
    ).first()

    if not reset_entry:
        logger.error("Invalid reset token")
        raise HTTPException(status_code=400, detail="Invalid token")

    user = db.query(User).filter(User.id == reset_entry.user_id).first()
    user.password = hash_password(data.new_password)

    db.delete(reset_entry)
    db.commit()

    logger.info(f"Password reset successful for user {user.id}")
    return {"message": "Password reset successful"}
