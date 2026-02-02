import re
def valid_emails(email_list):
    pattern=r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z0-9]+'
    for email in email_list:
        if re.match(pattern, email):
            yield email

emails = ["user@example.com", "invalid-email", "admin@test.org"]
for email in valid_emails(emails):
    print(email)
