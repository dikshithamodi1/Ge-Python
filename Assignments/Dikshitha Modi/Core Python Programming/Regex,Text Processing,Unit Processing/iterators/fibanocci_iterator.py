class FibanocciIterator:
    def __init__(self):
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b  # update state
        return value
fib = FibanocciIterator()

# Print first 10 Fibonacci numbers
for i, num in enumerate(fib):
    print(num, end=' ')
    if i >= 9:
        break