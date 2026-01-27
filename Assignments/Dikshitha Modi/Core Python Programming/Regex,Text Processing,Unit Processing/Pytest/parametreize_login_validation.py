import re
def login_validation(email):
    pattern=r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z0-9]+$'
    return bool(re.match(pattern,email))