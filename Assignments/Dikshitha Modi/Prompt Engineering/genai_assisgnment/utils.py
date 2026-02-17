# Exercise 3 — Test Generation

def divide(a, b):
    """
    Divides two numbers.

    Raises ValueError if denominator is zero.
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
