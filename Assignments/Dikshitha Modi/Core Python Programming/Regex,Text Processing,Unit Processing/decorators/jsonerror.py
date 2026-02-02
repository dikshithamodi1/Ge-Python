import json
from functools import wraps

def handle_json_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except json.JSONDecodeError as e:
            print(f"JSON error: {e}")
            return None
    return wrapper
@handle_json_error
def parse_data(data):
    return json.loads(data)
parse_data('{"a": 1}')        # works
parse_data('{"a": }')         # prints error, returns None
