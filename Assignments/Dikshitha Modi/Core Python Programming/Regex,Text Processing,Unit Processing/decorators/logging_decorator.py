import time
import functools

def timer_decorator(func):
    """Decorator to measure execution time of a function."""
    
    @functools.wraps(func)  # Preserves metadata of original function
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f}s")
        return result
    
    return wrapper


@timer_decorator
def slow_function():
    time.sleep(1)
    return "Done"


# Usage
print(slow_function())

