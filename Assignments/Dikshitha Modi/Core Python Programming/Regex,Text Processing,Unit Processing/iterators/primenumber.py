# Helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):#checking till square root of num
        if num % i == 0:
            return False
    return True

# Prime number iterator class
class PrimeNumberIterator:
    def __init__(self):
        self.n = 2  # Start checking from the first prime

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = self.n
            self.n += 1
            if is_prime(current):
                return current

# Example usage:
primes = PrimeNumberIterator()

# Print first 10 prime numbers
for i, p in enumerate(primes):
    print(p, end=' ')
    if i >= 9:  # stop after 10 primes
        break
