from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from datetime import timezone
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# -------------------
# CONFIG
# -------------------
SECRET_KEY = "fundoo-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Bearer security
security = HTTPBearer()

# -------------------
# CREATE TOKEN
# -------------------
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# -------------------
# VERIFY TOKEN
# -------------------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid Token")

        return email

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")
