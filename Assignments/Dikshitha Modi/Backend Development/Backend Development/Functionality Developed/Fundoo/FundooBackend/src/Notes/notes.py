from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Note
from schemas import NoteCreate, NoteUpdate, NoteOut
from auth import decode_access_token

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

# Dependency to get current user ID from JWT token
def get_current_user(token: str = Header(...)):
    user_id = decode_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user_id


# ---------------- CRUD Operations ----------------

# Create Note
@router.post("/", response_model=NoteOut)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)  # automatically get from JWT
):
    db_note = Note(**note.dict(), user_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


# Get All Notes for current user
@router.get("/", response_model=List[NoteOut])
def get_notes(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return db.query(Note).filter(Note.user_id == user_id).all()


# Get Single Note
@router.get("/{note_id}", response_model=NoteOut)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


# Update Note
@router.put("/{note_id}", response_model=NoteOut)
def update_note(
    note_id: int,
    note_data: NoteUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    for key, value in note_data.dict(exclude_unset=True).items():
        setattr(note, key, value)
    db.commit()
    db.refresh(note)
    return note


# Delete Note
@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == user_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"detail": "Note deleted successfully"}
