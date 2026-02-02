from functools import wraps

def retry(times=3):                 #  decorator factory
    """Decorator factory to retry a function 'times' times on exception."""
    def decorator(func):            # actual decorator
        @wraps(func)
        def wrapper(*args, **kwargs):  # wrapper executed at function call
            last_exception = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
            # If all attempts fail, raise the last exception
            raise last_exception
        return wrapper
    return decorator
@retry(times=3)
def test_network_call():
    # Simulate a flaky network test
    raise ConnectionError("Network down")

# Calling the function
test_network_call()
