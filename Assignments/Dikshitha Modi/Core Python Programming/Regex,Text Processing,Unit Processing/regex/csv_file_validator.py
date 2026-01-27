import re
def csv_file_validator(email):
    pattern=r'^[a-zA-Z0-9_.%+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        print(f"Valid : {email}")
    else:
        print(f"Invalid : {email}")
email=["alex@corp.com", "wrong.email@"]
for s in email:
    csv_file_validator(s)
