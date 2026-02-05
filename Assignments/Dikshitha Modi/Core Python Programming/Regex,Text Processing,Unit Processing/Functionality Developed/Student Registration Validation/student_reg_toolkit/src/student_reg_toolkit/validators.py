import re
import time
import logging
import sys
from functools import wraps

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_validation(func):
    """
    A decorator that logs the input, result, and execution time of a validation function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000  # ms
        input_value = args[0] if args else "N/A"
        validation_name = func.__name__
        log_message = (
            f"Validation '{validation_name}' for input '{input_value}': "
            f"Result={'PASSED' if result else 'FAILED'}, "
            f"Time={execution_time:.2f} ms"
        )
        logging.info(log_message)
        return result
    return wrapper


@log_validation
def validate_university_email(email: str) -> bool:
    """Validates if an email is a university email (contains '@' and ends with '.edu')."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.edu$"
    return bool(re.fullmatch(pattern, email))


@log_validation
def validate_student_id(student_id: str) -> bool:
    """Validates if a student ID is exactly 9 digits."""
    pattern = r"^\d{9}$"
    return bool(re.fullmatch(pattern, student_id))


@log_validation
def validate_password(password: str) -> bool:
    """Validates password rules: min 8 chars, at least 1 uppercase, at least 1 digit."""
    if not isinstance(password, str):
        return False
    min_length_pattern = r".{8,}"
    uppercase_pattern = r"[A-Z]"
    digit_pattern = r"\d"
    return (
        bool(re.search(min_length_pattern, password))
        and bool(re.search(uppercase_pattern, password))
        and bool(re.search(digit_pattern, password))
    )


def main_cli():
    """
    Main command-line interface for the registration validation toolkit.
    Validates a single email, ID, and password from command line arguments.
    """
    if len(sys.argv) != 4:
        print("Usage: reg-validate <email> <student_id> <password>")
        sys.exit(1)
    email_to_validate = sys.argv[1]
    id_to_validate = sys.argv[2]
    password_to_validate = sys.argv[3]
    print(f"\n--- Running Registration Validation for: {email_to_validate} ---")
    email_result = validate_university_email(email_to_validate)
    id_result = validate_student_id(id_to_validate)
    password_result = validate_password(password_to_validate)
    print(f"\nValidation Summary:")
    print(f"  Email '{email_to_validate}': {'VALID' if email_result else 'INVALID'}")
    print(f"  Student ID '{id_to_validate}': {'VALID' if id_result else 'INVALID'}")
    print(f"  Password (hidden): {'VALID' if password_result else 'INVALID'}")
    if email_result and id_result and password_result:
        print("\nOverall: ✅ All validations PASSED!")
        sys.exit(0)
    else:
        print("\nOverall: ❌ Some validations FAILED!")
        sys.exit(1)


if __name__ == "__main__":
    # Quick manual checks when executed directly
    print("--- Quick manual validator checks ---")
    validate_university_email("test@univ.edu")
    validate_university_email("invalid@gmail.com")
    validate_student_id("123456789")
    validate_student_id("123")
    validate_password("SecurePass1")
    validate_password("weakpass")
