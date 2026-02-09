import re

def validate_first_name(first_name: str) -> bool:
    pattern = r"^[A-Z][a-zA-Z]{2,}$"
    return bool(re.match(pattern, first_name))
