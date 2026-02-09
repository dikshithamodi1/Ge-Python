from uc3_email import validate_email

EMAIL_SAMPLES = [
    "abc@yahoo.com",
    "abc.100@abc.com.au",
    "abc@gmail.com.com",
    "abc",
    "abc@.com.my",
    "abc..2002@gmail.com"
]

def validate_email_samples():
    for email in EMAIL_SAMPLES:
        print(f"{email:30} -> {'VALID' if validate_email(email) else 'INVALID'}")
