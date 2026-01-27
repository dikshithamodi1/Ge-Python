def handle_error(error_type, value):
        error_handlers={
        "ValueError": lambda val : f"Handled by ValueError func with value '{val}'",
        "TypeError":lambda val: f"Handled by ValueError func with value '{val}'"
        }
        try:
            #trying to invoke error handler
            return error_handlers[error_type](value)
        except KeyError:
            return "Unknown"
        finally:
            print(f"Logging attempt to handle {error_type} with value '{value}'")
print(handle_error("ValueError", "bad")) 
