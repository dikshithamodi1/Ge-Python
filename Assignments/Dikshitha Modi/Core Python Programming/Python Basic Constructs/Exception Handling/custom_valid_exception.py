class InvalidAgeError(Exception):
    pass
def validate_age(age):
    if age<18 or age>100:
        raise InvalidAgeError(age)
    print("Valid")
validate_age(15)
