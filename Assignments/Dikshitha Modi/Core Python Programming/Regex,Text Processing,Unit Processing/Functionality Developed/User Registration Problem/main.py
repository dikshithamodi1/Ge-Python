from uc1_first_name import validate_first_name
from uc2_last_name import validate_last_name
from uc3_email import validate_email
from uc4_mobile import validate_mobile
from uc5_to_uc8_password import validate_password
from uc9_email_samples import validate_email_samples

def main():
    print("=== User Registration System ===")

    first = input("Enter First Name: ")
    print("UC1 Result:", validate_first_name(first))

    last = input("Enter Last Name: ")
    print("UC2 Result:", validate_last_name(last))

    email = input("Enter Email: ")
    print("UC3 Result:", validate_email(email))

    mobile = input("Enter Mobile (91 9919819801): ")
    print("UC4 Result:", validate_mobile(mobile))

    password = input("Enter Password: ")
    print("UC5–UC8 Result:", validate_password(password))

    print("\nUC9 Email Sample Validation:")
    validate_email_samples()

    print("\nThank You")

if __name__ == "__main__":
    main()
