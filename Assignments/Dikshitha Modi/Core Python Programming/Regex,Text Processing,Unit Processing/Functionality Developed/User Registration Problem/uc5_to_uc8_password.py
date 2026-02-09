import re

SPECIAL_CHARS = r"!@#$%^&*()_+\-=\{\}\[\]\|:;\"'<>,\.\?\/`~"

def validate_password(password: str) -> bool:
    # UC5: Minimum 8 characters
    if len(password) < 8:
        return False

    # UC6: At least 1 uppercase
    if not re.search(r"[A-Z]", password):
        return False

    # UC7: At least 1 numeric
    if not re.search(r"[0-9]", password):
        return False

    # UC8: Exactly 1 special character
    if len(re.findall(f"[{SPECIAL_CHARS}]", password)) != 1:
        return False

    return True
