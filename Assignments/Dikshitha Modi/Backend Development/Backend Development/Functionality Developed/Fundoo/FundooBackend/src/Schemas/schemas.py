from pydantic import BaseModel

# -------- AUTH --------
class RegisterRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


# -------- NOTES --------
class NoteCreate(BaseModel):
    title: str
    content: str | None = None


class NoteOut(NoteCreate):
    id: int

    class Config:
        from_attributes = True


# -------- PASSWORD RESET --------
class ForgotPasswordRequest(BaseModel):
    email: str


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
