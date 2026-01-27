import re
def form_validator(text):
    pattern=r'^Name:\s.+\nEmail:\s.+@.+\nPhone:\s\d+$'
    if re.findall(pattern,text):
        print("valid input")
    else:
        print("invalid input")
form_validator("Name: Alex\nEmail: alex@corp.com\nPhone: 9876543210")