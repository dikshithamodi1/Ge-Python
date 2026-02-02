class Singleton:
    def __init__(self, cls):
        self._cls = cls          # Store the decorated class
        self._instance = None    # Store the single instance

    def __call__(self, *args, **kwargs):
        # Create the instance if it doesn't exist
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        # Return the same instance on subsequent calls
        return self._instance
@Singleton
class DatabaseConnection:
    def __init__(self, host):
        self.host = host

db1 = DatabaseConnection("localhost")
db2 = DatabaseConnection("remotehost")

print(db1 is db2)  # True — same instance
print(db1.host)    # "localhost"
print(db2.host)    # "localhost" — second call ignored
