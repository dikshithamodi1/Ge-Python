import re

def validate_mobile(mobile: str) -> bool:
    pattern = r"^[0-9]{1,3}\s[0-9]{10}$"
    return bool(re.match(pattern, mobile))
