import re

def validate_last_name(last_name: str) -> bool:
    pattern = r"^[A-Z][a-zA-Z]{2,}$"
    return bool(re.match(pattern, last_name))
