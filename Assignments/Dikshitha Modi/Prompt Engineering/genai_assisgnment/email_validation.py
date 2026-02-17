# EXERCISE - 1

import re

def validate_email(email: str) -> bool:
    """
    Validates whether the provided string is a valid email address.

    Parameters:
    email (str): Email address to validate

    Returns:
    bool: True if valid email, False otherwise
    """

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


if __name__ == "__main__":
    # Valid emails
    print(validate_email("test@example.com"))
    print(validate_email("user.name@gmail.com"))

    # Invalid emails
    print(validate_email("testexample.com"))
    print(validate_email("user@"))
